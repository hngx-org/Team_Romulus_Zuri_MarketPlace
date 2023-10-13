from django.test import TestCase

# Create your tests here.

from rest_framework.test import APIClient
from MarketPlace.models import Shop, ProductCategory, Product, Wishlist,  UserProductRating, User
from django.urls import reverse
from django.urls import reverse
from rest_framework import status


class WishlistViewSetTest(TestCase):
    # databases='__all__'
    def setUp(self):
        self.client = APIClient()
        
        self.user = User.objects.create(
            username="testuser",
            first_name="John",
            last_name="Doe",
            email="test@example.com",
            password="testpassword",
            provider="example",
            location="Test Location",
            country="Test Country",
            profile_pic="profile.jpg",
            refresh_token="refreshtoken123",
        )
        
        
        self.product = Product.objects.create(
            shop=Shop.objects.create(
                name="Sample Shop",
                policy_confirmation=True,
                reviewed=True,
                rating=4.5
            ),
            name="Sample Product 1",
            description="Sample Description 1",
            quantity=10,
            category=ProductCategory.objects.create(
                name="Sample Category 1",
            ),
            price=100.00,
            discount_price=90.00,
            tax=10.00,
            is_published=True,
            currency="USD",
            rating=UserProductRating.objects.create(
                user_id=self.user,
                rating=5
            )
        )
        

    def test_create_wishlist_item(self):
        url = reverse("wishlist_create")
        data = {"product_id": str(self.product.id), "user_id": str(self.user.id)}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Product added to wishlist")
        self.assertIn("wishlist_item", response.data)
        print(response.data)
    
        
    def test_create_wishlist_item_existing(self):
        new_list = Wishlist.objects.create(user_id=self.user, product_id=self.product)
        url = reverse("wishlist_create")
        data = {"product_id": new_list.product.id, "user_id": new_list.user.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Product already in wishlist")
        print(response.data)
        
        
    def test_create_wishlist_item_invalid_product(self):
        url = reverse("wishlist_create")
        data = {"product_id": 999}  # Assuming a product with ID 999 doesn't exist
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["message"], "Product with provided id not found.")
        print(response.data)
        
        
    def test_create_wishlist_item_missing_product_id(self):
        url = reverse("wishlist_create")
        data = {}  # Missing "product_id" in the request data
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], '"product_id" required in the request data')
        
    def tearDown(self):
        self.user.delete()
        self.product.delete()