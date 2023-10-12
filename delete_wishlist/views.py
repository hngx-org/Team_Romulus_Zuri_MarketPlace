from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from MarketPlace.models import Wishlist
from .serializers import WishlistSerializer

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product_from_wishlist(request, product_id):
    # Check if the product is in the user's wishlist
    try:
        wishlist_item = Wishlist.objects.get(user=request.user, product_id=product_id)
    except Wishlist.DoesNotExist:
        return Response({'detail': 'Product not in the wishlist'}, status=status.HTTP_404_NOT_FOUND)

    # Delete the product from the wishlist
    wishlist_item.delete()

    return Response({'detail': 'Product removed from the wishlist'}, status=status.HTTP_204_NO_CONTENT)
