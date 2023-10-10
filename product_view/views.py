from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from product_view.models import ProductView, User, Product
from .serializers import ProductViewSerializer

class GetLastViewedProducts(APIView):
    @staticmethod
    def get(request, user_id):
        """Check if user exists."""
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'success': False, 'statusCode': 404, 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        """Get the list of products that the user has recently viewed."""
        product_views = ProductView.objects.filter(user_id=user_id).order_by('-timestamp')

        """If the user has not viewed any products recently, return an empty list."""
        if not product_views.exists():
            return Response({'success': True, 'statusCode': 200, 'message': 'No products viewed by the user', 'users': []})

        """Serialize the list of product views."""
        serializer = ProductViewSerializer(product_views, many=True)

        """Construct the final response."""
        response_data = {
            'success': True,
            'statusCode': 200,
            'message': f'{len(product_views)} Users retrieved successfully',
            'users': serializer.data
        }

        """Return the response in the desired format."""
        return Response(response_data)
