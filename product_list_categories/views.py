from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from MarketPlace.models import Product, ProductCategory
from .serializers import ProductSerializer
import random
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.



class ProductListByCategoryView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, categories):
        sort_by = request.query_params.get('sort_by', 'name')

        try:
            category = ProductCategory.objects.get(name=categories)
            products = Product.objects.filter(category_id=category).order_by(sort_by)
            
            
            if not products.exists():
                # Category exists but has no products, return an empty list
                return Response([], status=status.HTTP_200_OK)
                
            serializer = self.serializer_class(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProductCategory.DoesNotExist:
            return Response({'message': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
