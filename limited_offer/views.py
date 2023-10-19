from rest_framework import generics
from MarketPlace.models import Product
# from limited_offer.serializers import ProductSerializer
from all_products.serializers import AllProductSerializer as ProductSerializer
from rest_framework.response import Response
from rest_framework import status

class LimitedOfferListView(generics.ListAPIView):
    """
    View for listing limited offers with discounts.

    This view lists products with discounts available.

    Attributes:
    - serializer_class: The serializer class used to serialize the data.
    """

    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Get the queryset for products with discounts.

        Returns:
        - queryset: A filtered queryset containing products with discounts.
        """
        queryset = Product.objects.filter(
            discount_price__isnull=False,
            is_deleted='active',
            admin_status='approved'
        ).exclude(discount_price=0.00)
        return queryset

    def list(self, request, *args, **kwargs):
        """
        List limited offers with discounts.

        This method lists products with discounts and returns a JSON response.

        Args:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: JSON response containing the list of limited offers.
        """
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response({
                'status': 200,
                'success': True,
                'message': 'No discounts found.'
                }, status=status.HTTP_200_OK)
        
        try:
            serializer = self.get_serializer(queryset, many=True)
            response_data = {
                'status': 200,
                'success': True,
                'message': 'List of limited offers',
                'count': queryset.count(),
                'results': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            error_message = str(e)
            return Response({
                'error': error_message,
                'success': True,
                'status_code': 400
                }, status=status.HTTP_400_BAD_REQUEST)

