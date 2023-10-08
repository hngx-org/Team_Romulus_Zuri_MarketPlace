from django.urls import path, include
from  .views import SimilarProductView, FilterProductView, GetProductsSubCategories, ProductListByCategoryView, WishlistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wishlist', WishlistViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('products/<str:categories>', ProductListByCategoryView.as_view(), name='get_all_products_by_categories'),
    path('similar_products/<uuid:product_id>/', SimilarProductView.as_view(), name='similar-products'),
    path('products/', FilterProductView.as_view(), name='filter_products'),
    path('api/wishlist/<str:pk>/delete/', WishlistViewSet.as_view({'delete': 'destroy'}), name='wishlist-delete'),

    path('products/<str:category>/<str:subcategory>/', GetProductsSubCategories.as_view(), name='get_products_by_subcategories')

]