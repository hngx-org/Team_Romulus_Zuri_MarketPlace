from django.urls import path, include
from .views import SimilarProductView, FilterProductView, ProductListByCategoryView, WishlistProductsView, WishlistViewSet, Status, GetProductsSubCategories
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'wishlist', WishlistViewSet)


urlpatterns = [
    path('', Status.as_view(), name='status'),
    path('api/', include(router.urls)),
    path('similar_products/<uuid:product_id>/', SimilarProductView.as_view(), name='similar-products'),
    path('products/', FilterProductView.as_view(), name='filter_products'),
    path('wishlist/<str:pk>/delete/', WishlistViewSet.as_view({'delete': 'destroy'}), name='wishlist-delete'),
    path('wishlist/<slug:user_id>/', WishlistProductsView.as_view(), name='get_wishlist_product'),
    path('products/<str:category>/<str:subcategory>/', GetProductsSubCategories.as_view(), name='get_products_by_subcategories'),
    path('wishlist/', WishlistProductsView.as_view(), name='wishlist'),
]