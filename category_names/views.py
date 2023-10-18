from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from MarketPlace.models import ProductCategory, ProductSubCategory
from rest_framework import status
from .serializers import ProductCategorySerializer, ProductSubCategorySerializer



class CategoryNameView(APIView):
    def get(self, request):
        try:
            categories = ProductCategory.objects.all()
            category_data = []

            for category in categories:
                category_serializer = ProductCategorySerializer(category).data

                # Include subcategories within the category
                subcategories = ProductSubCategory.objects.filter(parent_category=category)
                subcategory_data = ProductSubCategorySerializer(subcategories, many=True).data
                category_serializer['subcategories'] = subcategory_data

                category_data.append(category_serializer)

            return Response({'message': 'Category names returned successfully', 'data': category_data}, status=status.HTTP_200_OK)
        except Exception as e:
            
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
