from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from MarketPlace.models import Product
from MarketPlace.serializers import ProductSerializer

# Create your views here.

from django.db.models import F
from django.db.models import FloatField
from django.db.models import Min
from django.db.models import Avg


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
            serializer = ProductSerializer(recommended_products, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



