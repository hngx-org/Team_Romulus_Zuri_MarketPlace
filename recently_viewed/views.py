from django.shortcuts import render



# Create your views here.

from django.http import Http404, JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.views import APIView
# from rest_framework.response import Response
# from MarketPlace.models import UserProductInteraction
# from .serializers import UserProductInteractionSerializer


# class RecentlyViewedProducts(APIView):
#     serializer_class = UserProductInteractionSerializer
#     def get(self, request, user_id):
#         try:
#             # Fetch recently viewed products for a specific user
#             recently_viewed = UserProductInteraction.objects.filter(
#                 user=user_id,
#                 interaction_type="viewed"
#             ).order_by('-createdat')

#             serializer = self.serializer_class(recently_viewed, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except UserProductInteraction.DoesNotExist:
#             return Response({'message': 'Recently viewed products not found'}, status=status.HTTP_404_NOT_FOUND)

from rest_framework.response import Response
from MarketPlace.models import UserProductInteraction
from .serializers import UserProductInteractionSerializer

class RecentlyViewedProducts(APIView):
    serializer_class = UserProductInteractionSerializer

    def get(self, request, user_id):
        try:
            # Fetch recently viewed products for a specific user
            recently_viewed = UserProductInteraction.objects.filter(
                user=user_id,
                interaction_type="viewed"
            ).order_by('-createdat')

            # Serialize the recently viewed interactions
            serializer = self.serializer_class(recently_viewed, many=True)
            response = {
                "message": "Request Sucessful",
                "status_code": 200,
                "data": serializer.data,
                "error": None,
                "success": True
            }

            # return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_200_OK)

        except UserProductInteraction.DoesNotExist:
            response = {
                "message": "Recently viewed products not found",
                "status_code": 404,
                "data": {'message': 'Recently viewed products not found'},
                "error": True,
                "success": False
            }
            # return Response({'message': 'Recently viewed products not found'}, status=status.HTTP_404_NOT_FOUND)
            return Response(response, status=status.HTTP_404_NOT_FOUND)
