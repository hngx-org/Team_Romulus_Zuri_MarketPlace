from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import ProductView
from .serializers import ProductViewSerializer

class GetLastViewedProducts(APIView):
    def get(self, request, user_id):
        # Check if the user exists
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Get the list of products that the user has recently viewed
        product_views = ProductView.objects.filter(user_id=user_id).order_by('-viewed_at')

        # If the user has not viewed any products recently, return an empty list
        if not product_views.exists():
            return Response([])

        # Serialize the list of product views
        serializer = ProductViewSerializer(product_views, many=True)

        # Return the serialized list of product views
        return Response(serializer.data)
