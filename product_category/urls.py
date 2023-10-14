from django.urls import path
from .views import ProductListByCategoryView


urlpatterns = [
        path('products/<str:category>', ProductListByCategoryView.as_view(), name='get_all_products_by_categories'),
 
]
