from django.shortcuts import render
from rest_framework import generics
from MarketPlace.models import LastViewedProduct, UserProductInteraction, User, Product
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.utils import timezone
from django.http import Http404
from .serializers import UserProductInteractionSerializer, ProductItemSerializer, ShopSerializer
import uuid
from rest_framework.decorators import api_view

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from . import docs

# Create your views here.
@swagger_auto_schema(methods=['post'],request_body= docs.product_by_list_body, responses=docs.product_by_list_resonses)
@api_view(['POST'])
def GetProductByIdList(request, *args, **kwargs):
    #product_ids = request.data['product_ids']
    try:
        if product_ids := request.data.get('product_ids', None):
            products = Product.objects.filter(id__in=product_ids)
            numberOfProducts = products.count()
            serializer = ProductItemSerializer(products, many=True)

            return Response ({
                'status': status.HTTP_200_OK,
                'success': True,
                'message': 'Request succesfull',
                'count': numberOfProducts,
                'data': serializer.data
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'success': False,
            'count': -1,
            'message': 'Empty or none existent product list, please provide a list of product ids in reqeust body',
            'data': {}
            }, status= status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'success': False,
            'count': -1,
            'message': str(e),
            'data': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateRecentlyViewd(generics.GenericAPIView):
    serializer_class = UserProductInteractionSerializer

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        product_id = kwargs.get('product_id')
        #this function attempts to create a recently viewed and returns a Response 
        query_response = addRecentlyViewed(user_id=user_id, product_id=product_id)
        return Response(query_response.data)        


class GetProductItem(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductItemSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        user_id = kwargs.get('user_id')
        product_id = kwargs.get('id')
        guest = request.query_params.get('guest')
    
        response_data = super().retrieve(request, *args, **kwargs)
        if guest == 'false':#user is logged in hence we update the recently viewed for that user
            qurery_response = addRecentlyViewed(user_id=user_id, product_id=product_id)#this function attempts to create a recently viewed and returns a Response
            if qurery_response.status_code != status.HTTP_201_CREATED:#this means there was a problem adding the product to recently viewed
                return Response(qurery_response.data, status= qurery_response.status_code)
            
        response_body = {
                'message': 'Product retrieved succesfully',
                'status': 200,
                'success': True,
                'data': response_data.data
            }
        return Response(response_body, status= status.HTTP_200_OK)

  

"""This function adds/updates the users recently viewed and returns a resonse object"""
def addRecentlyViewed(user_id, product_id):
    #getting the current time
    current_time = timezone.now()
    #constructing a data for the serializer
    serializer_data = {
        "user": user_id,
        "product": product_id,
        "interaction_type": "viewed",
        "createdat": current_time
    }

    #initailizing a serializer for the provided data
    serializer = UserProductInteractionSerializer(data=serializer_data)
    if serializer.is_valid():
        try: 
            user = User.objects.get(id = user_id)
        except ObjectDoesNotExist:
            return Response({'message', 'User not found'}, status= status.HTTP_404_NOT_FOUND)

        try:
            product = Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            return Response({'message': 'Product not found'}, status= status.HTTP_404_NOT_FOUND)
    

        last_viewed = LastViewedProduct.objects.filter(user=user)
        if last_viewed.exists():
            #deleting the previous last_viewed object corresponding to this user, user cant have two last viewed 
            last_viewed.delete()
        
        #creating a new last_viewed object
        last_viewed_object = LastViewedProduct.objects.create(user=user,product=product, viewed_at =current_time)
        last_viewed_object.save()

        recently_viewed = UserProductInteraction.objects.filter(user=user, product=product, interaction_type="viewed").order_by('-createdat')#getting the objects this user has recently viewed and sorting by date created in descending order
        if recently_viewed.exists():#user has previously viewed this same product so just update the timestamp to the current time
            if recently_viewed.count() > 1:#if for some reason user has more than one recently viewed item which is not supposed to be tho :]
                items_to_delete = recently_viewed[1:] #getting all the recently viewed starting from the second one
                items_to_delete.delete()#deleting the recent views with thesame user and thesame product because user cant recently view one product twice :)
            interaction = recently_viewed.first()
            interaction.createdat = current_time
            interaction.save()           
        else:#user doesnt have a recently viewed so we create one 
            serializer.save()

        context = {
            'message': 'History updated successfully',
            'status': 201,
            'success': True,
            'data': serializer.data
        }
        return Response(context, status= status.HTTP_201_CREATED)
    else:
        error_message = next(iter(serializer.errors.values()))[0]
        response_body = {
            'message': error_message,
            'success': False,
            'status': 400,
            'data': {}
        }
        return Response(response_body, status=status.HTTP_400_BAD_REQUEST)

    


    
    
