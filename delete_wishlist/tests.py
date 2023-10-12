# delete_wishlist/tests.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from MarketPlace.models import Product, Wishlist

class DeleteFromWishlistTestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        # Create a product
        self.product = Product.objects.create(id="your_product_id", name="Test Product", description="Product Description", quantity=10, price=100.0)

        # Create a wishlist item
        self.wishlist_item = Wishlist.objects.create(user=self.user, product=self.product)

        # Authenticate the user
        self.client.force_authenticate(user=self.user)

    def test_delete_product_from_wishlist(self):
        # Ensure the product exists in the user's wishlist
        self.assertEqual(Wishlist.objects.filter(user=self.user, product=self.product).count(), 1)

        # Send a DELETE request to remove the product from the wishlist
        url = reverse('delete_from_wishlist', args=[str(self.product.id)])
        response = self.client.delete(url)

        # Check if the response status code is 204 (No Content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure the product is no longer in the wishlist
        self.assertEqual(Wishlist.objects.filter(user=self.user, product=self.product).count(), 0)

    def test_delete_nonexistent_product_from_wishlist(self):
        # Send a DELETE request to remove a non-existent product from the wishlist
        non_existent_product_id = "non_existent_product_id"
        url = reverse('delete_from_wishlist', args=[non_existent_product_id])
        response = self.client.delete(url)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Ensure the wishlist is not modified
        self.assertEqual(Wishlist.objects.filter(user=self.user).count(), 1)
