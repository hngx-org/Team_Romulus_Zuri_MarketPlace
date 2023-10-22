from rest_framework.generics import ListAPIView
from MarketPlace.models import Product
from .serializers import AllProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .utils import (
	is_deleted_active,
	admin_status_approved,
	admin_approved_shop,
	shop_not_deleted,
	shop_not_restricted
)
from rest_framework.pagination import PageNumberPagination


class ProductListAPIView(ListAPIView):
	"""
	List All Products
	"""
	serializer_class = AllProductSerializer
	permission_classes = [AllowAny]

	def list(self, request):
		queryset = Product.objects.all().order_by('-updatedat')
		queryset = is_deleted_active(queryset)
		queryset = admin_status_approved(queryset)
		queryset = admin_approved_shop(queryset)
		queryset = shop_not_deleted(queryset)
		queryset = shop_not_restricted(queryset)
		paginator = PageNumberPagination()
		paginator.page_size = 10
		result = paginator.paginate_queryset(queryset, request)
		response = {
			'success': True,
			'status': 200,
			'error': None,
			'message': 'Sucessfully Fetched All Products',
			'data': self.get_serializer(result, many=True).data,
			"page_info": {
                "count": paginator.page.paginator.count,
                "next": paginator.get_next_link(),
                "previous": paginator.get_previous_link(),
            }
		}
		return Response(response, status=status.HTTP_200_OK)
