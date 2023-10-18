from rest_framework.views import APIView
from rest_framework.response import Response
from MarketPlace.models import Product
from all_products.serializers import AllProductSerializer as ProductSerializer
from django.db.models import Q

class ProductSearchView(APIView):

    def get(self, request):
        query = request.query_params.get('search', None)
        if not query:
            return Response({"status": "error", "message": "A search term must be provided."}, status=400)

        try:
            products = Product.objects.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query)
            )

            # If no products found, return an appropriate message
            # if not products.exists():
            #     return Response({"status": "error", "message": "No products found matching the search term."}, status=404)

            serializer = ProductSerializer(products, many=True)
            return Response({
                "status": "200",
                "message": f"Found {len(serializer.data)} products matching the search term.",
                "data": serializer.data,
            })

        except Exception as e:
            return Response({"status": "error", "message": f"An unexpected error occurred: {str(e)}"}, status=500)
