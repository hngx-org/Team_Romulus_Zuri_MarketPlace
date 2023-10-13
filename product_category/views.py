from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from MarketPlace.models import Product, ProductCategory, ProductSubCategory
from .serializers import ProductSerializer
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


class ProductListByCategoryView(APIView):
    def get(self, request, categories):
        # sort_by = request.query_params.get('sort_by', 'name')
        category = ProductCategory.objects.get(name=categories)
        products = Product.objects.filter(category=category)
        try:
            if not products:
                return Response({'message': 'The category exists, but has no products'}, status=status.HTTP_200_OK)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except category.DoesNotExist:
            return Response({'message': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

