from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from MarketPlace.models import ProductCategory
from rest_framework import status
from .serializers import ProductCategorySerializer

class CategoryNameView(APIView):
    def get(self, request):
        try:
            categories = ProductCategory.objects.all()
            category_names = set()  # To store unique category names
            serializer = []

            for category in categories:
                if category.name not in category_names:
                    serializer.append(ProductCategorySerializer(category).data)
                    category_names.add(category.name)

            return Response({'category': serializer}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)