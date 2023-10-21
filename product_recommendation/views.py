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


class ProductRecommendationView(APIView):
    def get(self, request):
        """
        List recommended products
        """
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
        """
        List similar products
        """
        try:
            current_product = Product.objects.get(id=product_id)

        except Product.DoesNotExist:
            response_data = {
                "status_code": 404,
                "message": "Product not found",
                "status": "error",
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        try:
            similar_products = Product.objects.filter(category=current_product.category).exclude(id=product_id)

            recommended_products = similar_products[:4]

            serializer = ProductSerializer(recommended_products, many=True)

            response_data = {
                "status_code": 200,
                "message": "Here are similar products",
                "data": {
                    "similar_products": serializer.data,
                },
                "status": "success",
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            response_data = {
                "status_code": 500,
                "message": f"An error occurred while retrieving similar product recommendations: {str(e)}",
                "status": "error",
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
