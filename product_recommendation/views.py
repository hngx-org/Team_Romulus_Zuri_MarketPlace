from django.shortcuts import render


# Create your views here.

from django.db.models import F
from django.db.models import FloatField
from django.db.models import Min
from django.db.models import Avg
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from MarketPlace.models import Product, ProductImage, User
from .serializers import ProductSerializer, ProductImageSerializer, UserSerializer

class ProductRecommendationView(APIView):
    def get(self, request):
        try:
            # Retrieve products with the highest quantity
            highest_quantity_products = Product.objects.order_by('-quantity')[:20]

            # Retrieve products with the highest discount price
            highest_discount_products = Product.objects.order_by('-discount_price')[:20]

            # Retrieve products with the highest rating
            highest_rated_products = Product.objects.filter(
                rating_id__isnull=False
            ).annotate(
                avg_rating=Avg('rating_id__rating', output_field=FloatField())
            ).order_by('-avg_rating')[:20]

            # Retrieve products with the lowest tax
            lowest_tax_products = Product.objects.annotate(
                lowest_tax=Min('tax')
            ).filter(
                tax=F('lowest_tax')
            )[:20]

            # Combine the recommendations without duplicates
            recommended_products = list(
                set(
                    highest_quantity_products |
                    highest_discount_products |
                    highest_rated_products |
                    lowest_tax_products
                )
            )[:20]

            # Serialize the recommended products
            product_serializer = ProductSerializer(recommended_products, many=True)
            
            # Add product images and user information to each product in the response
            for product_data in product_serializer.data:
                product_id = product_data['id']
                product = Product.objects.get(id=product_id)
                product_images = ProductImage.objects.filter(product=product)
                user = User.objects.get(id=product.user_id)

                product_data['product_images'] = ProductImageSerializer(product_images, many=True).data
                product_data['user'] = UserSerializer(user).data

            return Response(product_serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class SimilarProductRecommendationView(APIView):
    @staticmethod
    def get(request, product_id):
        try:
            current_product = Product.objects.get(id=product_id)

        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        similar_products = Product.objects.filter(category=current_product.category).exclude(id=product_id)

        recommended_products = similar_products[:4]

        serializer = ProductSerializer(recommended_products, many=True)

        return Response({'products': serializer.data}, status=status.HTTP_200_OK)

