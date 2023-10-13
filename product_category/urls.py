from django.urls import path, re_path
from .views import ProductListByCategoryView


urlpatterns = [
        # re_path(r'^api/products/(?P<category>[\w\s]+)/$', ProductListByCategoryView.as_view(), name='sample'),
        path('products/<str:categories>', ProductListByCategoryView.as_view(), name='get_all_products_by_categories'),
]
