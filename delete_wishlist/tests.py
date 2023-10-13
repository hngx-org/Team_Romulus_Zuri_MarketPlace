from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from MarketPlace.models import Wishlist
import uuid

class DeletewishlistAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')
        self.wishlist_item = Wishlist.objects.create(user_id=self.user.id, product_id=uuid.uuid4())

    def test_delete_wishlist_item(self):
        response = self.client.delete(f'/api/wishlist/{str(self.wishlist_item.product_id)}/')
        
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the wishlist item has been deleted from the database
        self.assertFalse(Wishlist.objects.filter(id=self.wishlist_item.id).exists())

    def test_delete_wishlist_item_invalid_uuid(self):
        response = self.client.delete('/api/wishlist/invalid-uuid/')
        
        # Check if the response status code is 400 Bad Request for an invalid UUID
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_delete_wishlist_item_not_found(self):
        non_existent_uuid = uuid.uuid4()  # Create a UUID that doesn't exist in the database
        response = self.client.delete(f'/api/wishlist/{str(non_existent_uuid)}/')
        
        # Check if the response status code is 404 Not Found for a non-existent item
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
