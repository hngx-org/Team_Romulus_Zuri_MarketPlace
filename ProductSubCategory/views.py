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
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        if not (product_id := self.kwargs.get('productId')):
            # Return all images when productId is not provided in the URL
            return ProductImage.objects.all()
        try:
            return ProductImage.objects.filter(product_id=product_id)
        except ProductImage.DoesNotExist:
            return Response(
                {"error": "ProductImage does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )



class GetProductsSubCategory(APIView):
    def get(self, request, category, subcategory):

        if not isinstance(category, str):
            return Response({"error": "Category name must be string"}, status=status.HTTP_400_BAD_REQUEST)
        if not isinstance(subcategory, str):
            return Response({"error": "Sub category name must be string"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            try:
                category_obj = ProductCategory.objects.get(name=category)
            except ProductCategory.DoesNotExist:
                return Response({"Message": f"There is no product category named {category}"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': e})

            try:
                ProductSubCategory.objects.filter(name=subcategory, parent_category=category_obj)
                prod = Product.objects.filter(category=category_obj, is_deleted='active')
                
            except ProductSubCategory.DoesNotExist:
                return Response({'error': f'There is no sub category named {subcategory} under {category}'})
            except Exception as e:
                return Response({'error': e})



            # Get products belonging to the provided subcategory
            # try:
            #     prod = Product.objects.filter(category=category_obj, is_deleted='active')
            #     #subCatProducts = Product.objects.filter(condition)

            # except Exception as e:
            #     return Response({"error": e}, status=status.HTTP_501_NOT_IMPLEMENTED)


            if not prod.exists():
                return Response({"products": [], "Message": "There are no products in this subCategory"}, status=status.HTTP_200_OK)

            serialized = ProductSerializer(prod,  many=True).data
            response = {
                "status": 200,
                "success": True,
                "message": f"Products of {subcategory} returned",
                "data": serialized
            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Server Malfunction {e}, we are fixing it'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# This endpoint will return categories names and the subcategories under them,
# with the respective data under each.

class catProducts(APIView):
    def get(self, request, categoryName):
        #get the category,subcat, products object
        try:
            category_obj = ProductCategory.objects.get(name=categoryName)
            subCat_obj = ProductSubCategory.objects.filter(parent_category=category_obj)
            products = Product.objects.filter(category=category_obj, is_deleted='active', admin_status='approved', is_published=True)
        except ProductCategory.DoesNotExist:
            return Response({
                'status': 404,
                'success': False,
                'message': f'The category {categoryName} does not exist',
                'data': None
                },
                            status=status.HTTP_404_NOT_FOUND
                )

        #get the subCats in the cat

        categoryResponse = []
        for subCat in subCat_obj:
            subCat = ProductsubCatSerializer(subCat).data
            subCat_products = []
            for product in products:
                product = ProductSerializers(product).data
                if product.get('category') == category_obj.id:
                    # the condition should be with respect to subcategory, but the model at this time does not have subcategory
                    if len(subCat_products) != 4:
                        #We want to display only four products
                        subCat_products.append(product)

            subcategoryData = {'name': subCat.get('name'), 'products': subCat_products}
            categoryResponse.append(subcategoryData)

        response = {
                'status': 200,
                'success': True,
                'message': f"Category {categoryName} and it's products",
                'data': categoryResponse
                }
        return Response(response, status=status.HTTP_200_OK)
