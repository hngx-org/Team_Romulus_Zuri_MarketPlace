from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductCategory, Wishlist
from .serializers import ProductSerializer, WishlistSerializer
import random
from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import ProductCategory


  


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

class ProductListByCategoryView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, categories):
        sort_by = request.query_params.get('sort_by', 'name')

        try:
            category = ProductCategory.objects.get(name=categories)
            products = Product.objects.filter(category=category).order_by(sort_by)
            
            
            if not products.exists():
                # Category exists but has no products, return an empty list
                return Response([], status=status.HTTP_200_OK)
                
            serializer = self.serializer_class(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProductCategory.DoesNotExist:
            return Response({'message': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
        


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
    
   
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    # Custom action to delete a product from the wishlist
    def destroy(self, request, *args, **kwargs):
        try:
            product_id = kwargs.get('pk')
            wishlist_item = Wishlist.objects.get(product_id=product_id)

            # Check if the user is authorized to delete this item (you may need to add your own logic)
            # For example, you can check if the user owns the wishlist item.

            # Delete the wishlist item
            wishlist_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Wishlist.DoesNotExist:
            return Response({'detail': 'Wishlist item not found.'}, status=status.HTTP_404_NOT_FOUND)
