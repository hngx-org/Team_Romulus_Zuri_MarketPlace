from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from MarketPlace.models import Product, ProductCategory
from .serializers import ProductSerializer
from django.db.models import Q


# Create your views here.
class FilterProductView(APIView):
    def get(self, request):
        # Parameters from request
        discount = self.request.query_params.get('discount')
        category = self.request.query_params.get('category')
        keywords = self.request.query_params.get('keywords')

        products = Product.objects.all()

        if discount:
            products = products.filter(discount_price__lte=discount)
        
        if category:
            products = products.filter(category_id__name=category)

        if keywords:
            products = products.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords))

        serializer = ProductSerializer(products, many=True)

        return Response({'products': serializer.data}, status=status.HTTP_200_OK)