from django.urls import path
from .views import GetImages, catProducts, GetProductsSubCategory
from . import error_handlers

# handler404 = 'ProductSubCategory.error_handlers.handle_404'
# handler500 = 'ProductSubCategory.error_handlers.handle_500'


urlpatterns = [
        path('products/category/<str:categoryName>', catProducts.as_view(), name='categoryProducts'),
        path('image/<productId>/', GetImages.as_view(), name='product-images'),
        path('images/', GetImages.as_view(), name='product-images'),
        path('products/<str:category>/<str:subcategory>/', GetProductsSubCategory.as_view(), name='product-sub-category'),
        # not working yet

]
