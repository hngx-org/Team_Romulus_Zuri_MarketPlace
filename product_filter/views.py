from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from MarketPlace.models import Product
from .serializers import AllProductSerializer
from django.db.models import Q
from django.http import Http404
from rest_framework.pagination import PageNumberPagination

# Custom Filters: Custom filtering classes.
class KeywordFilter:
    def filter(self, queryset, keywords):
        if keywords:
            return queryset.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords) | Q(category__name__icontains=keywords))
        return queryset

class CategoryFilter:
    def filter(self, queryset, category):
        if category:
            return queryset.filter(category__name=category)
        return queryset

class SubCategoryFilter:
    def filter(self, queryset, sub_category):
        if sub_category:
            return queryset.filter(category__productsubcategory__name=sub_category)
        return queryset
    
class DiscountFilter:
    def filter(self, queryset, discount):
        if discount:
            return queryset.filter(discount_price=discount)
        return queryset
    
class PriceFilter:
    def filter(self, queryset, min_price, max_price):
        if min_price and max_price:
            return queryset.filter(Q(price__gte=min_price) & Q(price__lte=max_price))
        return queryset

class RatingFilter:
    def filter(self, queryset, rating):
        if rating:
            return queryset.filter(rating_id__rating__gte=rating)
        return queryset
    
class HighestPriceFilter:
    def filter(self, queryset, highest_price):
        if highest_price:
            if highest_price == 'true':
                # Implement logic to order by highest price
                return queryset.order_by('-price')
            else:
                # Implement logic to order by lowest price
                return queryset.order_by('price')
        return queryset
    
# Custom Exceptions: Define custom exception classes for different error scenarios.
class InvalidFilterParams(Exception):
    def __init__(self, message="Invalid filter parameters"):
        self.message = message
        super().__init__(self.message)
    
# Create your views here.
class FilterProductView(APIView):

    # pagination_class = PageNumberPagination
    # page_size = 10
    
    def get(self, request):
        """
        Filter products by category, sub category, discount, keywords, rating, price, and highest price.
        """
        keyword_filter = KeywordFilter()
        category_filter = CategoryFilter()
        sub_category_filter = SubCategoryFilter()
        discount_filter = DiscountFilter()
        price_filter = PriceFilter()
        rating_filter = RatingFilter()
        highest_price_filter = HighestPriceFilter()

        try:
            products = Product.objects.all()

            # Parameters from request
            category = self.request.query_params.get("category")
            sub_category = self.request.query_params.get("sub_category")
            discount = self.request.query_params.get("discount")
            keywords = self.request.query_params.get("keywords")
            rating = self.request.query_params.get("rating")
            price = self.request.query_params.get("price")
            highest_price = self.request.query_params.get('highest_price')

       
            products = keyword_filter.filter(products, keywords)  
            products = category_filter.filter(products, category)
            products = sub_category_filter.filter(products, sub_category)   
            products = discount_filter.filter(products, discount)
            products = rating_filter.filter(products, rating)

            if price:
                min_price, max_price = price.split(",")
                products = price_filter.filter(products, min_price, max_price)

            products = highest_price_filter.filter(products, highest_price)

            if not products:
                response_data = {
                    "success": True,
                    "status": 200,
                    "error": None,
                    "message": "No products to display.",
                    "data": {"products": []}
                }
                return Response(response_data, status=status.HTTP_200_OK)
            
            paginator = PageNumberPagination()
            paginator.page_size = 10

            result_page = paginator.paginate_queryset(products, request)

            serializer = AllProductSerializer(result_page, many=True)

            response_data = {
                "success": True,
                "status": 200,
                "error": None,
                "message": "Filtered Products",
                "data": {
                    "products": serializer.data,
                    "page_info": {
                        "count": paginator.page.paginator.count,
                        "next": paginator.get_next_link(),
                        "previous": paginator.get_previous_link(),
                    }
                }
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except InvalidFilterParams as e:
            response_data = {
                "success": False,
                "status": 400,
                "error": str(e),
                "message": None,
                "data": None
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)               
        except Http404:
            response_data = {
                "success": False,
                "status": 404,
                "error": "Not Found",
                "message": None,
                "data": None

            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            response_data = {
                "success": False,
                "status": 400,
                "error": str(e),
                "message": None,
                "data": None
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
