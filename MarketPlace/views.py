from django.http import Http404, JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductCategory, ProductSubCategory, Wishlist
from .serializers import ProductSerializer, WishlistSerializer
from random import sample
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import View
from django.core.exceptions import ObjectDoesNotExist


class Status(APIView):
    def get(request):
        return Response({"Message": "API Endpoint server is Running"}, status=status.HTTP_200_OK)


class SimilarProductView(APIView):
    @staticmethod
    def get(request, product_id):
        try:
            current_product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        similar_products = Product.objects.filter(category_id=current_product.category_id).exclude(id=product_id)
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
            products = products.filter(category_id__name=category)

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
            products = Product.objects.filter(category_id=category).order_by(sort_by)
            
            
            if not products.exists():
                # Category exists but has no products, return an empty list
                return Response([], status=status.HTTP_200_OK)
                
            serializer = self.serializer_class(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProductCategory.DoesNotExist:
            return Response({'message': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
        


class GetProductsSubCategories(APIView):
    def get(self, request, category, subcategory):
        # Get the products related to the categories n sub categories
        try:
            category_obj = get_object_or_404(ProductCategory, name=category)
            subcategory_obj = get_object_or_404(ProductSubCategory, name=subcategory, parent_category_id=category_obj)

            # Get products belonging to the provided subcategory
            products = Product.objects.filter(subcategory_id=subcategory_obj)

            if not products:
                return Response({"Message": "There are no products in this subCategory"}, status=status.HTTP_200_OK)

            # Serialize the products
            serializer = ProductSerializer(products, many=True)
            return Response({'products': serializer.data}, status=status.HTTP_200_OK)
        except ProductSubCategory.DoesNotExist:
            return Response({"Message": "Subcategory does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
   
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

class WishlistProductsView(View):
    def get(self, request, user_id):
        wishlist_items = Wishlist.objects.filter(user_id=user_id)
        wishlist_data = []
        
        for item in wishlist_items:
            data = {
                'product_id': item.product_id,
                'created_at': item.created_at,     
            }
            wishlist_data.append(data)
        
        response_data = {'wishlist': wishlist_data}
        
        return JsonResponse(response_data)
    
class WishlistView(APIView):
    serializer_class = WishlistSerializer

    def post(self, request):

        if not request.data.get("product_id"):
            return Response({'message': '"product_id" required in the request data'}, status=status.HTTP_400_BAD_REQUEST)

        product_id = request.data.get("product_id")

        try:
            # Retrieve product details 
            product = Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            return Response({"message": "Product with provided id not found."}, status=status.HTTP_404_NOT_FOUND)

        # Add the product to the user's wishlist
        wishlist_item, created = Wishlist.objects.get_or_create(user_id=request.user.id, product_id=product)

        if created:
            serializer = self.serializer_class(wishlist_item)
            return Response({'message': 'Product added to wishlist', 'wishlist_item': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Product already in wishlist'}, status=status.HTTP_200_OK)

        
