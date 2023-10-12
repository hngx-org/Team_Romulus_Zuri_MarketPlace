from django.urls import path, include
from .views import SimilarProductView, Status, GetAllCategoriesName, FilterProductView, ProductListByCategoryView, WishlistProductsView, WishlistViewSet, Status, GetProductsSubCategories, PopularityBasedRecommendationView, GetImage
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'wishlist', WishlistViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('', Status.as_view(), name="status"),
    path('image/<imageId>', GetImage.as_view(), name='image'),
    path('categories', GetAllCategoriesName.as_view(), name="category_name"),
    path('products/<str:categories>', ProductListByCategoryView.as_view(), name='get_all_products_by_categories'),
    path('similar_products/<uuid:product_id>/', SimilarProductView.as_view(), name='similar-products'),
    path('products/', FilterProductView.as_view(), name='filter_products'),
    path('wishlist/<str:pk>/delete/', WishlistViewSet.as_view({'delete': 'destroy'}), name='wishlist-delete'),
    path('wishlist/<slug:user_id>/', WishlistProductsView.as_view(), name='get_wishlist_product'),
    path('products/<category>/<subcategory>/', GetProductsSubCategories.as_view(), name='get_products_by_subcategories'),
    path('wishlist/', WishlistProductsView.as_view(), name='wishlist'),
    path('recommendations/', PopularityBasedRecommendationView.as_view(), name='popularity_recommendations'),
]
