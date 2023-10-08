from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductCategory
from .models import Product
from .serializers import GetAllProductSerializer

class GetAllCategoriesProduct(APIView):
    serializer_class = GetAllProductSerializer
    def get(self, request, categories):
        sort_by = request.query_params.filter(sort_by='name')
        try:
            products = ProductCategory.objects.filter(name=categories).order_by(sort_by)
            serializer = self.serializer_class(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

  


