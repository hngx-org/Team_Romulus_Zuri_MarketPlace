from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from MarketPlace.models import Wishlist
import uuid

class DeleteWishlistItem(APIView):
    authentication_classes = []  # Requires authentication
    
    def delete(self, request, product_id):
        try:
            product_id = uuid.UUID(product_id)  # Validate the UUID
            item = get_object_or_404(Wishlist, product_id=product_id, user_id=request.user.id)
            item.delete()
            return Response({'message': 'Product removed from wishlist'}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'Invalid UUID format'}, status=status.HTTP_400_BAD_REQUEST)
        except Wishlist.DoesNotExist:
            return Response({'error': 'Product not found in wishlist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
