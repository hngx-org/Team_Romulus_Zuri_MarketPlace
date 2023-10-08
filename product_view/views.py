from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import ProductView
from .serializers import ProductViewSerializer

class GetLastViewedProducts(APIView):
    @staticmethod
    def get(self, request, user_id):
        """You can check if the user exists by using User Model 
        however, since I'd to comment it out since we're not making 
        use of User Model at the moment."""
        # try:
        #     user = User.objects.get(id=user_id)
        # except User.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)

        """Get the list of products that the user has recently viewed and also check if user exists."""
        try:
            product_views = ProductView.objects.filter(user_id=user_id).order_by('-timestamp')
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        """If the user has not viewed any products recently, return an empty list."""
        if not product_views.exists():
            return Response([])

        """Serialize the list of product views."""
        serializer = ProductViewSerializer(product_views, many=True)

        """Return the serialized list of product views."""
        return Response(serializer.data)