from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import F
#from product_view.models import ProductView, User
from MarketPlace.models import Product
# from .serializers import ProductSerializer
from all_products.serializers import AllProductSerializer as ProductSerializer



class SortProducts(APIView):
    def get(self, request, sorting_option):
        """
        Sort for products
        """
        try:
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
                'status': status.HTTP_200_OK,
                'success': True,
                'message': 'Products successfully sorted',
                'data': serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except KeyError:
            response_data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'success': False,
                'message': 'Bad Request',
                'data': {'error': 'Invalid sorting option'}
            }
            
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            response_data = {
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'success': False,
                'message': str(e),
                'data': {'error': 'An unexpected error occurred'}
            }
            
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)