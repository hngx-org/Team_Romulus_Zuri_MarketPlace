from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
import random


class SimilarProductView(APIView):
    @staticmethod
    def get(request, product_id):
        try:
            current_product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        similar_products = Product.objects.filter(category=current_product.category).exclude(id=product_id)

        similar_products = list(similar_products)
        random.shuffle(similar_products)

        recommended_products = similar_products[:4]

        serializer = ProductSerializer(recommended_products, many=True)

        return Response({'similar_products': serializer.data}, status=status.HTTP_200_OK)


