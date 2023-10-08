from django.test import TestCase
from django.urls import reverse
from product_view.models import ProductView
from django.contrib.auth.models import User
import uuid
from datetime import datetime, timedelta

class ProductViewTestCase(TestCase):

    def setUp(self):
        # Create a user for our tests
        self.user = User.objects.create(username="testuser", password="password123")

        # Create some sample product views for our user
        past_date = datetime.now() - timedelta(days=1)
        ProductView.objects.create(user_id=self.user.id, product_id=uuid.uuid4(), viewed_at=past_date)
        ProductView.objects.create(user_id=self.user.id, product_id=uuid.uuid4(), viewed_at=datetime.now())

    def test_get_last_viewed_products_exists(self):
        response = self.client.get(reverse('get_last_viewed_products', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        
        # Check the ordering (latest first)
        self.assertTrue(response.json()[0]['viewed_at'] > response.json()[1]['viewed_at'])

    def test_get_last_viewed_products_empty(self):
        # Create another user who hasn't viewed any products
        another_user = User.objects.create(username="anotheruser", password="password123")

        response = self.client.get(reverse('get_last_viewed_products', args=[another_user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

    def test_get_last_viewed_products_nonexistent_user(self):
        non_existent_user_id = 999999  # A non-existent user ID
        response = self.client.get(reverse('get_last_viewed_products', args=[non_existent_user_id]))
        self.assertEqual(response.status_code, 404)
