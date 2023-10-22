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
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class ProductRecommendationView(APIView):
    @swagger_auto_schema(
        manual_parameters=[],
        responses={
            200: openapi.Response(
                description="Recommended products",
            ),
            400: "Bad Request",
            500: "Internal Server Error",
        },
        operation_summary="Get a list of recommended products",
        operation_description="This endpoint returns a list of recommended products based on various criteria such as highest quantity, highest discount, highest rating, and lowest tax. The response includes product details.",
    )
    
    
    def get(self, request):
        try:
            recommended_products = self.get_recommended_products()
            serialized_data = ProductSerializer(recommended_products, many=True).data

            response_data = {
                'status': 200,
                'success': True,
                'message': 'Recommended products',
                'data': serialized_data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            error_response = {
                'status': 500,
                'success': False,
                'data': [],
                'error': str(e)
            }
            return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_recommended_products(self):
        highest_quantity_products = self.get_products_by_highest_quantity()
        highest_discount_products = self.get_products_by_highest_discount()
        highest_rated_products = self.get_products_by_highest_rating()
        lowest_tax_products = self.get_products_by_lowest_tax()

        return list(
            set(
                highest_quantity_products
                | highest_discount_products
                | highest_rated_products
                | lowest_tax_products
            )
        )[:20]

    def get_products_by_highest_quantity(self):
        return Product.objects.filter(
            admin_status='approved', is_deleted='active', shop__restricted='no'
        ).order_by('-quantity')[:20]

    def get_products_by_highest_discount(self):
        return Product.objects.filter(
            admin_status='approved', is_deleted='active', shop__restricted='no'
        ).order_by('-discount_price')[:20]

    def get_products_by_highest_rating(self):
        return Product.objects.filter(
            admin_status='approved', is_deleted='active', shop__restricted='no', rating_id__isnull=False
        ).annotate(avg_rating=Avg('rating_id__rating', output_field=FloatField())).order_by('-avg_rating')[:20]

    def get_products_by_lowest_tax(self):
        return Product.objects.filter(
            admin_status='approved', is_deleted='active', shop__restricted='no'
        ).annotate(lowest_tax=Min('tax')).filter(tax=F('lowest_tax'))[:20]
    

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
            similar_products = Product.objects.filter(
                category=current_product.category,
                is_deleted='active',
                admin_status='approved',  # Filter by admin_status = 'approved'
                # restricted='no',  # Filter by restricted = 'no'
                # shop__is_deleted=False,  # Filter by active shop, assuming 'shop' is a ForeignKey field
                # shop__is_active=True  # Filter by active shop
            ).exclude(id=product_id)

            recommended_products = similar_products[:4]

            serializer = ProductSerializer(recommended_products, many=True)

            response_data = {
                "status_code": 200,
                "message": "Here are similar products",
                "data": {
                    "similar_products": serializer.data
                },
                "status": "success",
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                "status_code": 500,
                "message": f"An error occurred while retrieving product recommendations: {str(e)}",
                "status": "error",
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

