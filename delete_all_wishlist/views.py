from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from MarketPlace.models import Wishlist, User
import uuid

class DeleteAllWishlistItems(APIView):
    authentication_classes = []  # Requires authentication
    
    def delete(self, request, user_id):
        """
        Delete all items from a user's wishlist
        """
        try:
            # Validate the user_id as a UUID
            user_id = uuid.UUID(user_id)
            user = get_object_or_404(User, id=user_id)

            # Delete all items from the user's wishlist
            Wishlist.objects.filter(user=user).delete()

            return Response({
                'message': 'All items have been removed from this user\'s wishlist',
                'status_code': 200,
                'success': True
            }, status=status.HTTP_200_OK)

        except ValueError:
            return Response({
                'error': 'Not a valid UUID format',
                'success': True,
                'status_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({
                'error': 'User not found',
                'success': True,
                'status_code': 404
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'error': 'Internal Server Error',
                'success': True,
                'status_code': 500
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
