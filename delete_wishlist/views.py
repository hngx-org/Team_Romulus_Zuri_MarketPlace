from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
import uuid
from .models import Wishlist


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_from_wishlist(request, product_id):
    try:
        # Check if the product_id is a valid UUID
        uuid.UUID(str(product_id))
    except ValueError:
        raise ValidationError('Invalid UUID format for product_id')

    try:
        # Check if the product exists in the wishlist of the logged-in user
        wishlist_item = Wishlist.objects.get(user=request.user, product_id=product_id)
    except Wishlist.DoesNotExist:
        return Response({'message': 'Product not found in your wishlist.'}, status=status.HTTP_NOT_FOUND)

    # Delete the product from the wishlist
    wishlist_item.delete()

    return Response({'message': 'Product removed from your wishlist.'}, status=status.HTTP_204_NO_CONTENT)

# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.exceptions import ValidationError
# import uuid
# from .models import Wishlist
# from .decorators import skip_authentication  # Import the skip_authentication decorator

# # Apply the skip_authentication decorator to the view
# @api_view(['DELETE'])
# @skip_authentication
# def delete_from_wishlist(request, product_id):
#     try:
#         # Check if the product_id is a valid UUID
#         uuid.UUID(str(product_id))
#     except ValueError:
#         raise ValidationError('Invalid UUID format for product_id')

#     try:
#         # Check if the product exists in the wishlist of the logged-in user
#         wishlist_item = Wishlist.objects.get(user=request.user, product_id=product_id)
#     except Wishlist.DoesNotExist:
#         return Response({'message': 'Product not found in your wishlist.'}, status=status.HTTP_NOT_FOUND)

#     # Delete the product from the wishlist
#     wishlist_item.delete()

#     return Response({'message': 'Product removed from your wishlist.'}, status=status.HTTP_204_NO_CONTENT)
