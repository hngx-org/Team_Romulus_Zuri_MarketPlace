from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Wishlist

@override_settings(DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}})
class WishlistAPITest(TestCase):
    databases = {'default'}  # Add this line to specify the database alias

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')
        self.product_id = 1

        # Create a wishlist item for the user
        Wishlist.objects.create(user=self.user, product_id=self.product_id)

    def test_delete_product_from_wishlist(self):
        response = self.client.delete(f'/api/wishlist/{self.product_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_product_not_in_wishlist(self):
        response = self.client.delete('/api/wishlist/999/')  # A product that doesn't exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Product not in the wishlist')

    # Add more test cases for authentication, error handling, etc.
