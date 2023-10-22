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
<<<<<<< HEAD
        if not (product_id := self.kwargs.get('productId')):
            # Use get() method to avoid KeyError
=======
        product_id = self.kwargs.get('productId')  # Use get() method to avoid KeyError
        if product_id:
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
        else:
            # Return all images when productId is not provided in the URL
>>>>>>> 45be63a4b109e292fb0f1e1b1a7affb451b366fb
            return ProductImage.objects.all()
        try:
            return ProductImage.objects.filter(product_id=product_id)
        except ProductImage.DoesNotExist:
            return Response(
                {"error": "ProductImage does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        



<<<<<<< HEAD
# class GetImage(APIView):
#     def get(self, request, productId):
#         try:
#             images = ProductImage.objects.get(product=productId)
#             response = {
#                     'message': 'This is the url to where the image is hosted',
#                     'url': images.url
#                 }
#             return Response(response, status=status.HTTP_200_OK)
#         except ProductImage.DoesNotExist:
#             return Response({"error": "ProductImage does not exist"})


# class subCat(ListAPIView):
#     def get(self, request, cat, Subcat):
#         page = request.GET.get('page', 1)
#         items_per_page = request.GET.get('itemsPerPAge', 10)
#         offset = (int(page) - 1) * int(items_per_page)

#         products = Product.objects.filter(is_deleted='active')
#         paginator = Paginator(products, items_per_page)
#         try:
#             try:
#                 products = paginator.page(page)
#             except PageNotAnInteger:
#                 products = paginator.page(1)
#             except EmptyPage:
#                 products = paginator.page(paginator.num_pages)
        
#             product_data = []

#             for product in products:
#                 categories = []
#                 selected_categories = product.selected_categories.all()
#                 for sel_cat in selected_categories:
#                     sub_category = sel_cat.sub_category
#                     categories.append({
#                     'id': sel_cat.product_category.id,
#                     'name': sel_cat.product_category.name,
#                     'sub_categories': {
#                         'id': sub_category.id,
#                         'name': sub_category.name,
#                         'parent_category_id': sub_category.parent_category,
#                     }
#                 })
#             promo_product = product.promo_product

#             product_data.append({
#                 'id': product.id,
#                 'category': product.category,
#                 'name': product.name,
#                 'decsription': product.name,
#                 'quantity': product.quantity,
#                 'price': product.price,
#                 'discount_price': product.discount_price,
#                 'tax': product.tax,
#                 'admin_status': product.admin_status,
#                 'is_published': product.is_published,
#                 'is_deleted': product.is_deleted,
#                 'currency': product.currency,
#                 'createdat': product.createdat,
#                 'updatedat': product.updateat,
#                 'category': categories,
#                 'promo': promo_product,
#             })

#             response_data = {
#                 'data': {
#                     'itemsPerPage': int(items_per_page),
#                     'page': int(page),
#                     'totalPages': paginator.num_pages,
#                     'totalProducts': paginator.count,
#                     'products': product_data,

#                 }
#             }

#             # catId = ProductCategory.objects.filter(name=cat)
#             # subCat = ProductSubCategory.objects.filter(name=Subcat, parent_category=catId)
#             # products = Product.objects.filter(is_deleted='active')
#             # for product in products:
#             #     selected = SelectedCategories(sub_category=subCat, product_category=catId, product=products)
#             return Response(response_data)

#         except Exception as e:
#             return Response({"error": f"Exception raised {e}"})

=======
>>>>>>> 45be63a4b109e292fb0f1e1b1a7affb451b366fb
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
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            try:
                ProductSubCategory.objects.filter(name=subcategory, parent_category=category_obj)
                prod = Product.objects.filter(category=category_obj, is_deleted='active', admin_status='approved', is_published=True)
                
            except ProductSubCategory.DoesNotExist:
                return Response({
                    "status": 404,
                    "success": False,
                    "message": f'There is no sub category named {subcategory} under {category}'
                    }, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({
                    "status": 500,
                    "success": False,
                    "message": e
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            if not prod.exists():
                return Response({
                    "status": 200,
                    "success": True,
                    "message": "There are no products in this subCategory",
                    "data": []
                    }, status=status.HTTP_200_OK)

            page = request.GET.get('page', 1)
            items_per_page = request.GET.get('itemsPerPage', 5)
            offset = (int(page) - 1) * int(items_per_page)

            paginator = Paginator(prod, items_per_page)
            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)

            serialized = ProductSerializer(products,  many=True).data
            
            response = {
                "status": 200,
                "success": True,
                "message": f"Products of {subcategory} returned",
                "page_number": int(page),
                "items_per_page": int(items_per_page),
                "total_products": paginator.count,
                "total_pages": paginator.num_pages,
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

            # Get subcategories related to the category
            subCat_obj = ProductSubCategory.objects.filter(parent_category=category_obj)
            subCat_serializer = ProductsubCatSerializer(subCat_obj, many=True).data

            # Loop through subcategories
            for subcategory in subCat_serializer:
                subcategoryData = {
                    'name': subcategory['name'],
                    'products': []
                }

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

                subcategoryData['products'] = products_serializer
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

