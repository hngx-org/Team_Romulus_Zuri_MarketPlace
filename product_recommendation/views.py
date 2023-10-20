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
# from .serializers import ProductImageSerializer, UserSerializer, ProductSerializer
from all_products.serializers import AllProductSerializer as ProductSerializer
from django.core.exceptions import ObjectDoesNotExist

class ProductRecommendationView(APIView):
    def get(self, request):
        try:
            # Retrieve products with the highest quantity
            highest_quantity_products = Product.objects.filter(admin_status='approved', is_deleted='active', shop__restricted='no').order_by('-quantity')[:20]

            # Retrieve products with the highest discount price
            highest_discount_products = Product.objects.filter(admin_status='approved', is_deleted='active', shop__restricted='no').order_by('-discount_price')[:20]

            # Retrieve products with the highest rating
            highest_rated_products = Product.objects.filter(
                admin_status='approved', is_deleted='active', shop__restricted='no', rating_id__isnull=False
            ).annotate(
                avg_rating=Avg('rating_id__rating', output_field=FloatField())
            ).order_by('-avg_rating')[:20]

            # Retrieve products with the lowest tax
            lowest_tax_products = Product.objects.filter(admin_status='approved', is_deleted='active', shop__restricted='no').annotate(
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

            response_data = {
                'status': 200,
                'success': True,
                'message': 'Recommended products',
                'data': product_serializer.data
            }
            
            # Add product images and user information to each product in the response
            # for product_data in product_serializer.data:
            #     product_id = product_data['id']
            #     product = Product.objects.get(id=product_id)
            #     product_images = ProductImage.objects.filter(product=product)
            #     user = User.objects.get(id=product.user_id)

            #     product_data['product_images'] = ProductImageSerializer(product_images, many=True).data
            #     product_data['user'] = UserSerializer(user).data

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            response_data = {
                'status': 500,
                'success': False,
                'data': [],
                'error': str(e)
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


 

class SimilarProductRecommendationView(APIView):

    def get(self, request, product_id):
        
        try:
            current_product = Product.objects.get(id=product_id)
            
            # Create a subquery to get IDs of products in the same category
            similar_product_ids = Product.objects.filter(
                category=current_product.category
            ).exclude(id=product_id).values_list('id', flat=True)[:4]

            # Use the subquery to retrieve the similar products
            similar_products = Product.objects.filter(id__in=similar_product_ids)
            
            serializer = ProductSerializer(similar_products, many=True)

            response_data = {
                'status_code': 200,

                'message': 'Here are similar products',
                'data': {
                    'similar_products': serializer.data,
                },
                'status': 'success',
            }

            return Response(response_data, status=status.HTTP_200_OK)
    
        except ObjectDoesNotExist:
                response_data = {
                    'status_code': 404,
                    'message': 'Product not found',
                    'data': [],
                    'status': 'error',
                }
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Log the exception for debugging
            response_data = {
                'status': 'error',
                'message': f'An unexpected error occurred: {str(e)}',
                'data': {'error': str(e)}
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


















# class ProductRecommendationView(APIView):
#     def get(self, request):
#         try:
#             # Retrieve products with the highest quantity
#             highest_quantity_products = Product.objects.order_by('-quantity')[:20]

#             # Retrieve products with the highest discount price
#             highest_discount_products = Product.objects.order_by('-discount_price')[:20]

#             # Retrieve products with the highest rating
#             highest_rated_products = Product.objects.filter(
#                 rating_id__isnull=False
#             ).annotate(
#                 avg_rating=Avg('rating_id__rating', output_field=FloatField())
#             ).order_by('-avg_rating')[:20]

#             # Retrieve products with the lowest tax
#             lowest_tax_products = Product.objects.annotate(
#                 lowest_tax=Min('tax')
#             ).filter(
#                 tax=F('lowest_tax')
#             )[:20]

#             # Combine the recommendations without duplicates
#             recommended_products = list(
#                 set(
#                     highest_quantity_products |
#                     highest_discount_products |
#                     highest_rated_products |
#                     lowest_tax_products
#                 )
#             )[:20]

#             # Serialize the recommended products
#             product_serializer = ProductSerializer(recommended_products, many=True)

#             response_data = {
#                 'status': 200,
#                 'success': True,
#                 'message': 'Recommended products',
#                 'data': product_serializer.data
#             }
            
#             # Add product images and user information to each product in the response
#             # for product_data in product_serializer.data:
#             #     product_id = product_data['id']
#             #     product = Product.objects.get(id=product_id)
#             #     product_images = ProductImage.objects.filter(product=product)
#             #     user = User.objects.get(id=product.user_id)

#             #     product_data['product_images'] = ProductImageSerializer(product_images, many=True).data
#             #     product_data['user'] = UserSerializer(user).data

#             return Response(response_data, status=status.HTTP_200_OK)

#         except Exception as e:
#             response_data = {
#                 'status': 500,
#                 'success': False,
#                 'data': [],
#                 'error': str(e)
#             }
#             return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
