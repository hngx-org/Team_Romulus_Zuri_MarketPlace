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

            products = Product.objects.all()

            if discount:
                products = products.filter(discount_price__lte=discount)

            if category:
                products = products.filter(category_id__name=category)

            if sub_category:
                products = products.filter(
                    category__productsubcategory__name=sub_category
                )

            if keywords:
                products = products.filter(
                    Q(name__icontains=keywords) | Q(description__icontains=keywords)
                )

            if rating:
                products = products.filter(rating_id__rating__gte=rating)

            if price:
                min_price, max_price = price.split(",")
                products = products.filter(
                    Q(price__gte=min_price) & Q(price__lte=max_price)
                )

            if not products:
                return Response({"message": "No products to display."}, status=status.HTTP_200_OK)

            serializer = AllProductSerializer(products, many=True)

            return Response({"products": serializer.data}, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
