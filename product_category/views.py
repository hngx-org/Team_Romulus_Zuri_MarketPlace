from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from MarketPlace.models import Product, ProductCategory, ProductSubCategory
# from .serializers import ProductSerializer
from all_products.serializers import AllProductSerializer as ProductSerializer
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator


class ProductListByCategoryView(APIView):
    def get(self, request, category):
        # sort_by = request.query_params.get('sort_by', 'name')
        product_category = ProductCategory.objects.get(name=category)
        products = Product.objects.filter(category=product_category)

        if not isinstance(category, str):
            return Response({"error": "Category name must be a string value"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if not products:
                return Response({"products": [], 'message': 'The category exists, but has no products'},
                                status=status.HTTP_200_OK)
            serializer = ProductSerializer(products, many=True)
            return Response({'message': 'success', 'products': serializer.data}, status=status.HTTP_200_OK)
        except ProductCategory.DoesNotExist:
            return Response({'message': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': e})

