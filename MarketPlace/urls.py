

    

from django.urls import path
from  .views import SimilarProductView, FilterProductView, ProductListByCategoryView

urlpatterns = [
    path('products/<str:categories>', ProductListByCategoryView.as_view()),
    path('similar_products/<uuid:product_id>/', SimilarProductView.as_view(), name='similar-products'),
    path('products/', FilterProductView.as_view(), name='filter_products'),

]