from django.shortcuts import render
from MarketPlace.models import Product, ProductImage, ProductCategory, ProductSubCategory, SelectedCategories
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import ProductsubCatSerializer, ProductImageSerializer, ProductSerializers
from all_products.serializers import AllProductSerializer as ProductSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

# Create your views here.


class GetImages(ListAPIView):
    """
    Get product image
    """
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        if not (product_id := self.kwargs.get('productId')):
            # Return all images when productId is not provided in the URL
            return ProductImage.objects.all()
        try:
            return ProductImage.objects.filter(product_id=product_id)
        except ProductImage.DoesNotExist:
            return Response(
                {
                    "status_code": 404,
                    "error": True,
                    "message": "ProductImage does not exist"
                    },
                status=status.HTTP_404_NOT_FOUND,
            )



class GetProductsSubCategory(APIView):
    def get(self, request, category, subcategory):
        """
        Get products by sub category
        """

        if not isinstance(category, str):
            return Response({
                "status": 400,
                "success": False,
                "message": "Category name must be string"
                }, status=status.HTTP_400_BAD_REQUEST)
        if not isinstance(subcategory, str):
            return Response({
                "status": 400,
                "success": False,
                "message": "Sub category name must be string"
                }, status=status.HTTP_400_BAD_REQUEST)

        try:
            try:
                category_obj = ProductCategory.objects.get(name=category)
            except ProductCategory.DoesNotExist:
                return Response({
                    "status": 404,
                    "success": False,
                    "message": f"There is no product category named {category}"
                    }, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({
                    "status": 500,
                    "success": False,
                    "message": e
                    })

            try:
                ProductSubCategory.objects.filter(name=subcategory, parent_category=category_obj)
                prod = Product.objects.filter(category=category_obj, is_deleted='active')
                
            except ProductSubCategory.DoesNotExist:
                return Response({
                    "status": 404,
                    "success": False,
                    "message": f'There is no sub category named {subcategory} under {category}'
                    }, status=status.HTTP_404_OT_FOUND)
            except Exception as e:
                return Response({
                    "status": 500,
                    "success": False,
                    "message": e
                    })



            # Get products belonging to the provided subcategory
            # try:
            #     prod = Product.objects.filter(category=category_obj, is_deleted='active')
            #     #subCatProducts = Product.objects.filter(condition)

            # except Exception as e:
            #     return Response({"error": e}, status=status.HTTP_501_NOT_IMPLEMENTED)


            if not prod.exists():
                return Response({
                    "status": 200,
                    "success": True,
                    "message": "There are no products in this subCategory",
                    "data": []
                    }, status=status.HTTP_200_OK)

            serialized = ProductSerializer(prod,  many=True).data
            response = {
                "status": 200,
                "success": True,
                "message": f"Products of {subcategory} returned",
                "data": serialized
            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "status": 500,
                "success": False,
                "message": f'Server Malfunction: {e}'
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class catProducts(APIView):
    def get(self, request, categoryName):
        """
        This endpoint will return categories names and the subcategories under them,
        with the respective data under each.
        """
        # Initialize the category response list
        categoryResponse = []

        # Get the category object

        try:
            try:
                category_obj = ProductCategory.objects.get(name=categoryName)
            except ProductCategory.DoesNotExist:
                return Response({
                    'status': 404,
                    'success': False,
                    'message': f'The category {categoryName} does not exist',
                    'data': None
                }, status=status.HTTP_404_NOT_FOUND)

            # Get su   bcategories related to the category
            subCat_obj = ProductSubCategory.objects.filter(parent_category=category_obj)
            subCat_serializer = ProductsubCatSerializer(subCat_obj, many=True).data

            # Loop through subcategories
            for subcategory in subCat_serializer:
                # Filter products based on the category, will need to change ths to subcategory, once it is in the model
                products = Product.objects.filter(
                    category=category_obj,
                    #subcategory=subcategory['id'],  # Adjust this filter once you have subcategory support
                    is_deleted='active',
                    admin_status='approved',
                    is_published=True
                )[:4]  # Limit to four products

                # Serialize the filtered products
                products_serializer = ProductSerializer(products, many=True).data

                subcategoryData = {
                    'name': subcategory['name'],
                    'products': products_serializer,
                }
                categoryResponse.append(subcategoryData)

            response = {
                'status': 200,
                'success': True,
                'message': f"Category {categoryName} and its products",
                'data': categoryResponse
            }

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                'status': 500,
                'success': True,
                'message': f"An error occured {e}"
            }
            )



