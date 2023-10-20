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
    """
    Get product by id
    """
    #product_ids = request.data['product_ids']
    try:
        if product_ids := request.data.get('product_ids', None):
            products = Product.objects.filter(id__in=product_ids)
            numberOfProducts = products.count()
            serializer = ProductItemSerializer(products, many=True)

            return Response({
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
        """
        Create a recently viewed product
        """
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
        """
        Get recently viewed products
        """
        try:
            instance = self.get_object()
        except Http404:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        user_id = kwargs.get('user_id')
        product_id = kwargs.get('id')
        guest = request.query_params.get('guest')
        
        if instance.is_deleted != 'active':#this means product is not active, return
            return Response({
                'message': 'This product is not available',
                'success': False,
                'status': status.HTTP_503_SERVICE_UNAVAILABLE,
                'data': {}
                }, status= status.HTTP_503_SERVICE_UNAVAILABLE)
        
        if instance.admin_status != 'approved':#this means product is not approved, return
            return Response({
                'message': 'This product is pending approval',
                'success': False,
                'status': status.HTTP_503_SERVICE_UNAVAILABLE,
                'data': {}
                }, status= status.HTTP_503_SERVICE_UNAVAILABLE)
        
        if instance.shop.restricted != 'no':#this means shop is restricted, return
           return Response({
                'message': 'Shop is under restriction',
                'success': False,
                'status': status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
                'data': {}
                }, status= status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)

        response_data = super().retrieve(request, *args, **kwargs)
        #user is logged in hence we update the recently viewed for that user
        if guest == 'false':
            #this function attempts to create a recently viewed and returns a Response
            qurery_response = addRecentlyViewed(user_id=user_id, product_id=product_id)
            #this means there was a problem adding the product to recently viewed
            if qurery_response.status_code != status.HTTP_201_CREATED:
                return Response(qurery_response.data, status= qurery_response.status_code)
            
        response_body = {
                'message': 'Product retrieved succesfully',
                'status': 200,
                'success': True,
                'data': response_data.data
            }
        return Response(response_body, status= status.HTTP_200_OK)


def addRecentlyViewed(user_id, product_id):
    """
    This function adds/updates the users recently viewed and returns a resonse object.
    """
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

        #getting the objects this user has recently viewed and sorting by date created in descending order
        recently_viewed = UserProductInteraction.objects.filter(user=user, product=product, interaction_type="viewed").order_by('-createdat')
        #user has previously viewed this same product so just update the timestamp to the current time
        if recently_viewed.exists():
            #if for some reason user has more than one recently viewed item which is not supposed to be tho :]
            if recently_viewed.count() > 1:
                #getting all the recently viewed starting from the second one
                items_to_delete = recently_viewed[1:]
                #deleting the recent views with thesame user and thesame product because user cant recently view one product twice :)
                items_to_delete.delete()
            interaction = recently_viewed.first()
            interaction.createdat = current_time
            interaction.save()   
        #user doesnt have a recently viewed so we create one         
        else:
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

    
