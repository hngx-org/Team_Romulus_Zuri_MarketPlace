from django.urls import path, re_path
from .views import ProductListByCategoryView


urlpatterns = [
        path('products/<str:categories>', ProductListByCategoryView.as_view(), name='get_all_products_by_categories'),
]
