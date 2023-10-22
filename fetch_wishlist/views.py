# from django.http import JsonResponse, HttpResponseServerError
from rest_framework.generics import ListAPIView
from .serializers import WishlistSerializer
from MarketPlace.models import Wishlist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


class WishlistProductsView(ListAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

    def list(self, request, user_id):
        """
        List Wishlist
        """
        try:
            queryset = Wishlist.objects.filter(user_id=user_id, product__is_deleted="active", product__admin_status = "approved")
            if not queryset.exists():
                response = {
                    "message": "Wishlist is empty",
                    "status_code": 200,
                    "data": [],
                }
                return Response(response, status=status.HTTP_200_OK)

            serializer = self.get_serializer(queryset, many=True)
            response = {
                "message": "successfully fetched wishlist",
                "status_code": 200,
                "data": serializer.data
            }
            # return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                "message": "internal server error",
                "status_code": 500,
                "data": {'detail': str(e)},
            }
            return Response(response,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
