from rest_framework.generics import ListAPIView
from MarketPlace.models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny



class ProductListAPIView(ListAPIView):
	queryset = Product.objects.all().order_by('-updatedat')
	serializer_class = ProductSerializer
	permission_classes = [AllowAny]