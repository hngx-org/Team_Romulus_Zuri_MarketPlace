# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from MarketPlace.models import Wishlist, User, Product
# import uuid

# class DeleteWishlistItem(APIView):
#     authentication_classes = []  # Requires authentication
    
#     def delete(self, request, user_id, product_id):
#         try:
#             # Validate the user_id and product_id as UUIDs
#             user_id = uuid.UUID(user_id)
#             product_id = uuid.UUID(product_id)
            
#             # Check if the user exists
#             user = get_object_or_404(User, id=user_id)
            
#             # Check if the product is in the user's wishlist
#             item = get_object_or_404(Wishlist, product_id=product_id, user=user)
#             item.delete()
            
#             return Response({'message': 'Product removed from wishlist'}, status=status.HTTP_200_OK)
#         except ValueError:
#             return Response({'error': 'Invalid UUID format'}, status=status.HTTP_400_BAD_REQUEST)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
#         except Wishlist.DoesNotExist:
#             return Response({'error': 'Product not found in user\'s wishlist'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             print(e)
#             return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from MarketPlace.models import Wishlist, User
import uuid

class DeleteWishlistItem(APIView):
    authentication_classes = []  # Requires authentication
    
    def delete(self, request, user_id, product_id):
        try:
            # Validate the user_id and product_id as UUIDs
            user_id = uuid.UUID(user_id)
            product_id = uuid.UUID(product_id)

            # Check if the user exists
            user = get_object_or_404(User, id=user_id)

            if item := Wishlist.objects.filter(
                user=user, product_id=product_id
            ).first():
                item.delete()
                return Response({'message': 'Product removed from wishlist'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Product not found in user\'s wishlist'}, status=status.HTTP_404_NOT_FOUND)

        except ValueError:
            return Response({'error': 'Invalid UUID format'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
