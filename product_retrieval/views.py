from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from MarketPlace.models import Product
from all_products.serializers import AllProductSerializer as ProductSerializer
from django.db.models import Q

class ProductSearchView(APIView):

    def get(self, request):
        """
        Search for a product
        """
        query = request.query_params.get('search', None)
        if not query:
            return Response({"status": "error", "message": "A search term must be provided."}, status=400)

        try:
            products = Product.objects.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query)
            )

            # Pagination
            paginator = PageNumberPagination()
            paginated_products = paginator.paginate_queryset(products, request)
            
            serializer = ProductSerializer(paginated_products, many=True)
            
            return paginator.get_paginated_response({
                "status": 200,
                "message": f"Found {len(serializer.data)} products matching the search term.",
                "data": serializer.data,
            })

        except Exception as e:
            return Response({"status": "error", "message": f"An unexpected error occurred: {str(e)}"}, status=500)
