from django.shortcuts import render
from MarketPlace.models import Product, ProductImage, ProductCategory, ProductSubCategory
from MarketPlace.serializers import ProductSerializer
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class GetCategoryNames(APIView):
    '''This class will return the names of all the categories in the database'''

    def get(self, request):
        '''Return the categories'''
        categories = ProductCategory.objects.all()
        name = []
        for cat in categories:
            if cat not in name:
                name.append(cat.name)
        return Response({"categories name": name}, status=status.HTTP_200_OK)

class GetImage(APIView):
    def get(self, request, imageId):
        try:
            images = ProductImage.objects.get(id=imageId)
            response = {
                    'message': 'This is the url to where the image is hosted',
                    'url': images.url
                }
            return Response(response, status=status.HTTP_200_OK)
        except ProductImage.DoesNotExist:
            return Response({"error": "ProductImage does not exist", "reason": "Beans has been cooked"})

class GetProductsSubCategory(APIView):
    def get(self, request, category, subcategory):
        # Get the products related to the categories n sub categories
        # set the number of items to return per pages
        page_size = request.GET.get('page_size', 3)

        if not isinstance(category, str):
            return Response({"error": "Category name must be string"}, status=status.HTTP_400_BAD_REQUEST)
        if not isinstance(subcategory, str):
            return Response({"error": "Sub category name must be string"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            try:
                category_obj = ProductCategory.objects.get(name=category)
            except ProductCategory.DoesNotExist:
                return Response({"Message": f"There is no product category named {category}"}, status=status.HTTP_404_NOT_FOUND)

            try:
                subcategory_obj = ProductSubCategory.objects.get(name=subcategory, parent_category_id=category_obj)
            except ProductSubCategory.DoesNotExist:
                return Response({'error': f'There is no sub category named {subcategory} under {category}'})



            # Get products belonging to the provided subcategory
            products = Product.objects.filter(subcategory_id=subcategory_obj).order_by('category_id')

            if not products.exists():
                return Response({"products": [], "Message": "There are no products in this subCategory"}, status=status.HTTP_200_OK)

            # pagination
            pagination = Paginator(products, page_size)
            page_number = request.GET.get('page')
            products_per_page = pagination.get_page(page_number)
            serializer = ProductSerializer(products_per_page, many=True)
            return Response({'products': serializer.data}, status=status.HTTP_200_OK)

        except ProductSubCategory.DoesNotExist:
            return Response({"Message": "Subcategory does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Server Malfunction, we are fixing it', 'Note': 'Akjesus would not be proud'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
