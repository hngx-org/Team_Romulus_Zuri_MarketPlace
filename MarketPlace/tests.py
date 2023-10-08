from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import UserProfile, UserProductInteraction, Product

from django.contrib.auth.models import User  # Import User model

class RecommendationAPITest(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

        # Create user profiles for test users
        UserProfile.objects.create(user=self.user1, age=25, gender='male')
        UserProfile.objects.create(user=self.user2, age=30, gender='female')

        # Create test products
        self.product1 = Product.objects.create(name='Product 1', description='Description of Product 1', category='Electronics', price=499.99)
        self.product2 = Product.objects.create(name='Product 2', description='Description of Product 2', category='Clothing', price=39.99)
        self.product3 = Product.objects.create(name='Product 3', description='Description of Product 3', category='Electronics', price=799.99)

        # Create test user-product interactions
        UserProductInteraction.objects.create(user=self.user1, product=self.product1, interaction_type='viewed')
        UserProductInteraction.objects.create(user=self.user1, product=self.product2, interaction_type='purchased')
        UserProductInteraction.objects.create(user=self.user2, product=self.product1, interaction_type='viewed')
        UserProductInteraction.objects.create(user=self.user2, product=self.product3, interaction_type='viewed')


    def test_recommendations_endpoint(self):
        # Test the recommendations/<int:user_id>/ endpoint

        # Replace with a valid user_id
        user_id = self.user1.id
        url = reverse('recommendations', args=[user_id])
        client = APIClient()
        response = client.get(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more specific tests based on your recommendation logic
        # For now, let's check if the response is not empty
        self.assertNotEqual(len(response.data), 0)

    def test_invalid_user_id(self):
        # Test the recommendations/<int:user_id>/ endpoint with an invalid user_id
        url = reverse('recommendations', args=[999])  # Assuming user with ID 999 doesn't exist
        client = APIClient()
        response = client.get(url)

        # Check if the response status code is 404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Add more test cases as needed to cover different scenarios and edge cases
