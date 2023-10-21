from django.core.paginator import Paginator
from django.db.models import Q, Value, CharField
from django.db.models.functions import Replace, Concat
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from MarketPlace.models import Product
from all_products.serializers import AllProductSerializer as ProductSerializer


class ProductSearchRateThrottle(UserRateThrottle):
    rate = '50/hour'


class ProductSearchView(APIView):
    throttle_classes = [ProductSearchRateThrottle]

    def get(self, request):
        """
        Search for a product
        """
        query = request.query_params.get('search', None)
        if not query:
            return Response({"status": "error", "message": "A search term must be provided."}, status=400)

        try:
            # Highlighting logic
            highlighted_name = Replace('name', Value(query), Value(f'<mark>{query}</mark>'))
            highlighted_description = Replace('description', Value(query), Value(f'<mark>{query}</mark>'))

            products = Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            ).annotate(
                highlighted_name=Concat(Value('<span>'), highlighted_name, Value('</span>'), output_field=CharField()),
                highlighted_description=Concat(Value('<span>'), highlighted_description, Value('</span>'), output_field=CharField())
            ).order_by('id')

            # Manual Pagination
            page = request.query_params.get('page', 1)
            paginator = Paginator(products, 10)  # 10 items per page
            current_page = paginator.get_page(page)

            serializer = ProductSerializer(current_page, many=True)

            # Building the paginated response
            response_data = {
                "status": 200,
                "message": f"Found {len(serializer.data)} products matching the search term.",
                "data": serializer.data,
                "pagination": {
                    "next_page_number": current_page.next_page_number() if current_page.has_next() else None,
                    "previous_page_number": current_page.previous_page_number() if current_page.has_previous() else None,
                    "total_pages": paginator.num_pages,
                    "current_page": page
                }
            }

            return Response(response_data)

        except Exception as e:
            return Response({"status": "error", "message": f"An unexpected error occurred: {str(e)}"}, status=500)
