from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductCategory, Wishlist
from .serializers import ProductSerializer
import random
from django.db.models import Q, Wishlist
from django.shortcuts import get_object_or_404
from django.views import View


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

        return Response({'products': serializer.data}, status=status.HTTP_200_OK)

class FilterProductView(APIView):
    def get(self, request):
        # Parameters from request
        discount = self.request.query_params.get('discount')
        category = self.request.query_params.get('category')
        keywords = self.request.query_params.get('keywords')

        products = Product.objects.all()

        if discount:
            products = products.filter(discount_price__lte=discount)
        
        if category:
            products = products.filter(category=category)

        if keywords:
            products = products.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords))

        serializer = ProductSerializer(products, many=True)

        return Response({'products': serializer.data}, status=status.HTTP_200_OK)

class GetProductsSubCategories(APIView):
    def get(self, category, subcategory):
        # Get the products related to the categories n sub categories
        category_obj = get_object_or_404(ProductCategory, name=category)
        subcategory_obj = get_object_or_404(ProductCategory, name=subcategory, parent_category=category_obj)

        # Get products belonging to the provided subcategory
        products = Product.objects.filter(category=subcategory_obj)

        # Serialize the products
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data}, status=status.HTTP_200_OK)


class WishlistProductsView(View):
    def get(self, request, user_id):
        wishlist_items = Wishlist.objects.filter(user_id=user_id)
        wishlist_data = []
        
        for item in wishlist_items:
            data = {
                'product_id': item.product_id.id,
                'created_at': item.created_at,     
            }
            wishlist_data.append(data)
        
        response_data = {'wishlist': wishlist_data}
        
        return JsonResponse(response_data)
