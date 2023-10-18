from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from MarketPlace.models import Product
from .serializers import AllProductSerializer
from django.db.models import Q
from django.http import Http404


# Create your views here.
class FilterProductView(APIView):
    def get(self, request):
        try:
            # Parameters from request
            category = self.request.query_params.get("category")
            sub_category = self.request.query_params.get("sub_category")
            discount = self.request.query_params.get("discount")
            keywords = self.request.query_params.get("keywords")
            rating = self.request.query_params.get("rating")
            price = self.request.query_params.get("price")
            highest_price = self.request.query_params.get('highest_price')

            products = Product.objects.all()

            if discount:
                products = products.filter(discount_price=discount)

            if category:
                products = products.filter(category__name=category)

            if sub_category:
                products = products.filter(
                    category__productsubcategory__name=sub_category
                )

            if keywords:
                products = products.filter(
                    Q(name__icontains=keywords) | Q(description__icontains=keywords) |
                    Q(category__name__icontains=keywords)
                )

            if rating:
                products = products.filter(rating_id__rating__gte=rating)

            if price:
                min_price, max_price = price.split(",")
                products = products.filter(
                    Q(price__gte=min_price) & Q(price__lte=max_price)
                )

            if highest_price:
                if highest_price == 'true':
                    products = products.order_by('-price')
                else:
                    products = products.order_by('price')

            if not products:
                response_data = {
                    "success": True,
                    "status": 200,
                    "data": {"products": []},
                    "error": None,
                    "message": "No products to display."
                }
                return Response(response_data, status=status.HTTP_200_OK)

            serializer = AllProductSerializer(products, many=True)

            response_data = {
                "success": True,
                "status": 200,
                "data": {"products": serializer.data},
                "error": None,
                "message": "Filtered Products"
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Http404:
            response_data = {
                "success": False,
                "status": 404,
                "data": None,
                "error": "Not Found",
                "message": None
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            response_data = {
                "success": False,
                "status": 400,
                "data": None,
                "error": str(e),
                "message": None
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
