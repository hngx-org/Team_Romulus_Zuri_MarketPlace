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
        category = self.request.query_params.get('category')
        sub_category = self.request.query_params.get('sub_category')
        discount = self.request.query_params.get('discount')
        keywords = self.request.query_params.get('keywords')
        rating = self.request.query_params.get('rating')
        price = self.request.query_params.get('price')

        products = Product.objects.all()

        if discount:
            products = products.filter(discount_price__lte=discount)
        
        if category:
            products = products.filter(category_id__name=category)

        if sub_category:
            products = products.filter(subcategory_id__name=sub_category)

        if keywords:
            products = products.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords))

        if rating:
            products = products.filter(rating_id__rating__gte=rating)

        if price:
            min_price, max_price = price.split(',')
            products = products.filter(Q(price__gte=min_price) & Q(price__lte=max_price))

        serializer = ProductSerializer(products, many=True)

        return Response({'products': serializer.data}, status=status.HTTP_200_OK)