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
        """
        List Product by Category
        """
        # sort_by = request.query_params.get('sort_by', 'name')
        if not isinstance(category, str):
            return Response({"error": "Category name must be a string value"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            product_category = ProductCategory.objects.get(name=category)
            products = Product.objects.filter(category=product_category, is_deleted='active', admin_status='approved', shop__restricted='no')

            if not products.exists():
                return Response({"status": 200, "success": True, "data": [],
                                 'message': 'The Category exists, but has no products'},
                                status=status.HTTP_200_OK)
            serializer = ProductSerializer(products, many=True)

            return Response({"status": 200, "success": True,
                             'message': 'Products successfully returned based on the given category',
                             'data': serializer.data},
                            status=status.HTTP_200_OK)
        except ProductCategory.DoesNotExist:
            return Response({"status": 404, "success": False, 'message': 'Category does not exist.'},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"status": 500, "success": False, 'error': str(e), "message": f"An unexpected error occurred: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
