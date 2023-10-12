from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status
from .models import Product,  Wishlist
from .serializers import  WishlistSerializer
from django.core.exceptions import ObjectDoesNotExist


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
    
    def create(self, request):

        if not request.data.get("product_id"):
            return Response({'message': 'product required in the request data'}, status=status.HTTP_400_BAD_REQUEST)

        product_id = request.data.get("product_id")

        try:
            # Retrieve product details 
            product = Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            return Response({"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        # Add the product to the user's wishlist
        wishlist_item, created = Wishlist.objects.get_or_create(user_id=request.user.id, product_id=product_id)

        if created:
            serializer = self.serializer_class(wishlist_item)
            return Response({'message': 'Product added to wishlist', 'wishlist_item': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Product already exists in wishlist'}, status=status.HTTP_200_OK)