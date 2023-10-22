from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from MarketPlace.models import UserProductInteraction
from .serializers import UserProductInteractionSerializer

class RecentlyViewedProducts(APIView):
    serializer_class = UserProductInteractionSerializer

    def get(self, request, user_id):
        """
        Fetch recently viewed products for a specific user
        """
        try:
            # Fetch recently viewed products for a specific user
            recently_viewed = UserProductInteraction.objects.filter(
                user=user_id,
                interaction_type="viewed"
            ).order_by('-createdat')

            # Serialize the recently viewed interactions
            serializer = self.serializer_class(recently_viewed, many=True)
            response = {
                "message": "Request Successful",
                "status_code": 200,
                "data": serializer.data,
                "error": None,
                "success": True
            }

            return Response(response, status=status.HTTP_200_OK)

        except UserProductInteraction.DoesNotExist:
            response = {
                "message": "Recently viewed products not found",
                "status_code": 404,
                "data": {'message': 'Recently viewed products not found'},
                "error": 'Recently viewed products not found',
                "success": False
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, user_id):
        """
        Delete recently viewed products for a specific user
        """
        try:
            # Delete recently viewed products for a specific user
            deleted_count, _ = UserProductInteraction.objects.filter(
               user=user_id,
               interaction_type="viewed"
            ).delete()

            if deleted_count > 0:
                response = {
                    "message": "Recently viewed products deleted successfully",
                    "status_code": 200,
                    "data": {'deleted_count': deleted_count},
                    "error": None,
                    "success": True
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    "message": "No recently viewed products to delete",
                    "status_code": 404,
                    "data": {'message': 'No recently viewed products to delete'},
                    "error": 'No recently viewed products to delete',
                    "success": False
                }
                return Response(response, status=status.HTTP_404_NOT_FOUND)

        except UserProductInteraction.DoesNotExist:
            response = {
                "message": "Recently viewed products not found",
                "status_code": 404,
                "data": {'message': 'Recently viewed products not found'},
                "error": 'Recently viewed products not found',
                "success": False
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
