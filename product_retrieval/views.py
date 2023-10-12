from rest_framework.views import APIView
from rest_framework.response import Response
from MarketPlace.models import Product
from .serializers import ProductSerializer
from django.db.models import Q

class ProductSearchView(APIView):

    def get(self, request):
        query = request.query_params.get('search', None)
        if not query:
            return Response({"error": "A search term must be provided."}, status=400)

        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
        
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
