from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import F
#from product_view.models import ProductView, User
from MarketPlace.models import Product
# from .serializers import ProductSerializer
from all_products.serializers import AllProductSerializer as ProductSerializer

# class GetLastViewedProducts(APIView):
#     @staticmethod
#     def get(request, user_id):
#         """Check if user exists."""
#         try:
#             user = User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return Response({'success': False, 'statusCode': 404, 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#         """Get the list of products that the user has recently viewed."""
#         product_views = ProductView.objects.filter(user_id=user_id).order_by('-timestamp')

#         """If the user has not viewed any products recently, return an empty list."""
#         if not product_views.exists():
#             return Response({'success': True, 'statusCode': 200, 'message': 'No products viewed by the user', 'users': []})

#         """Serialize the list of product views."""
#         serializer = ProductViewSerializer(product_views, many=True)

#         """Construct the final response."""
#         response_data = {
#             'success': True,
#             'statusCode': 200,
#             'message': f'{len(product_views)} Users retrieved successfully',
#             'users': serializer.data
#         }

#         """Return the response in the desired format."""
#         return Response(response_data)

class SortProducts(APIView):
    def get(self, request, sorting_option):
        """
        Sort for products
        """
        # Validate the sorting option
        valid_sorting_options = [
            'name_asc', 'name_desc',
            'date_created_asc', 'date_created_desc',
            'price_asc', 'price_desc'
        ]

        if sorting_option not in valid_sorting_options:
            return Response({'success': False, 'statusCode': 400, 'message': 'Invalid sorting option'}, status=status.HTTP_400_BAD_REQUEST)

        # Map the sorting option to the corresponding field and order
        sorting_mapping = {
            'name_asc': 'name',
            'name_desc': '-name',
            'date_created_asc': 'createdat',
            'date_created_desc': '-createdat',
            'price_asc': 'price',
            'price_desc': '-price'
        }

        sorting_field = sorting_mapping[sorting_option]

        # Retrieve and sort the products based on the selected sorting option
        products = Product.objects.all().order_by(sorting_field)

        # Serialize the sorted products
        serializer = ProductSerializer(products, many=True)

        # Construct the final response
        response_data = {
            'status': 200,
            'success' : True,
            'message': 'Carts added',
            'data': serializer.data
        }

        return Response(response_data)
