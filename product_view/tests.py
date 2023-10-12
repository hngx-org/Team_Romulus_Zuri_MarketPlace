from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

# class ProductViewTestCase(TestCase):

#     def setUp(self):
#         # Create a user for our tests
#         self.user = User.objects.create(username="testuser", password="password123")

#         # Create some sample product views for our user
#         past_date = datetime.now() - timedelta(days=1)
#         ProductView.objects.create(user_id=self.user.id, product_id=uuid.uuid4(), viewed_at=past_date)
#         ProductView.objects.create(user_id=self.user.id, product_id=uuid.uuid4(), viewed_at=datetime.now())

#     def test_get_last_viewed_products_exists(self):
#         response = self.client.get(reverse('get_last_viewed_products', args=[self.user.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.json()), 2)
        
#         # Check the ordering (latest first)
#         self.assertTrue(response.json()[0]['viewed_at'] > response.json()[1]['viewed_at'])

#     def test_get_last_viewed_products_empty(self):
#         # Create another user who hasn't viewed any products
#         another_user = User.objects.create(username="anotheruser", password="password123")

#         response = self.client.get(reverse('get_last_viewed_products', args=[another_user.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.json()), 0)

#     def test_get_last_viewed_products_nonexistent_user(self):
#         non_existent_user_id = 999999  # A non-existent user ID
#         response = self.client.get(reverse('get_last_viewed_products', args=[non_existent_user_id]))
#         self.assertEqual(response.status_code, 404)



class SortProductsTestCase(TestCase):
    def setUp(self):
        # Initialize the client
        self.client = APIClient()

    def test_sort_by_name_asc(self):
        url = reverse('sort_products', args=['name_asc'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       
    def test_sort_by_name_desc(self):
        url = reverse('sort_products', args=['name_desc'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)       

    def test_sort_by_date_created_asc(self):
        url = reverse('sort_products', args=['date_created_asc'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_sort_by_date_created_desc(self):
        url = reverse('sort_products', args=['date_created_desc'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sort_by_price_asc(self):
        url = reverse('sort_products', args=['price_asc'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       
    def test_sort_by_price_desc(self):
        url = reverse('sort_products', args=['price_desc'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_sorting_option(self):
        url = reverse('sort_products', args=['invalid_option'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



