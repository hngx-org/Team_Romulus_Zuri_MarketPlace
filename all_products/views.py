from rest_framework.generics import ListAPIView
from MarketPlace.models import Product
from .serializers import AllProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status



class ProductListAPIView(ListAPIView):
	queryset = Product.objects.all().order_by('-updatedat')
	serializer_class = AllProductSerializer
	permission_classes = [AllowAny]

	def list(self, request):
		queryset = self.get_queryset()
		response = {
			'success': True,
			'status': 200,
			'data': self.get_serializer(queryset, many=True).data,
			'error': None,
			'message': 'Sucessfully Fetched All Products',
		}
		return Response(response, status=status.HTTP_200_OK)