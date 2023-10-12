from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import F
from product_view.models import ProductView, User
from MarketPlace.models import Product
from .serializers import ProductViewSerializer, ProductSerializer
from .utilities import SortingOptions

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


class SortProducts(APIView):
    @staticmethod
    def get(request):
        # Get the sorting option from query parameters
        sorting_option = request.query_params.get('sorting_option')

        # Validate the sorting option
        valid_sorting_options = [
            SortingOptions.NAME_ASC, SortingOptions.NAME_DESC,
            SortingOptions.DATE_CREATED_ASC, SortingOptions.DATE_CREATED_DESC,
            SortingOptions.PRICE_ASC, SortingOptions.PRICE_DESC
        ]

        if sorting_option not in valid_sorting_options:
            return Response({'success': False, 'statusCode': 400, 'message': 'Invalid sorting option'}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve and sort the products based on the selected sorting option
        products = Product.objects.all()

        if sorting_option == SortingOptions.NAME_ASC:
            products = products.order_by('name')
        elif sorting_option == SortingOptions.NAME_DESC:
            products = products.order_by('-name')
        elif sorting_option == SortingOptions.DATE_CREATED_ASC:
            products = products.order_by('created_at')
        elif sorting_option == SortingOptions.DATE_CREATED_DESC:
            products = products.order_by('-created_at')
        elif sorting_option == SortingOptions.PRICE_ASC:
            products = products.order_by('price')
        elif sorting_option == SortingOptions.PRICE_DESC:
            products = products.order_by('-price')

        # Serialize the sorted products
        serializer = ProductSerializer(products, many=True)

        # Construct the final response
        response_data = {
            'success': True,
            'statusCode': 200,
            'message': f'{len(products)} products retrieved successfully',
            'products': serializer.data
        }

        return Response(response_data)
