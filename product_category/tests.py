from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from MarketPlace.models import Product, ProductCategory

class ProductListByCategoryViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_products_by_category(self):
        category = ProductCategory.objects.create(name="Test Category")
        product1 = Product.objects.create(name="Product 1", category=category, is_deleted='active', admin_status='approved')
        product2 = Product.objects.create(name="Product 2", category=category, is_deleted='active', admin_status='approved')
        url = reverse('https://staging.zuri.team/api/marketplace/v1/products/Test-Category/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 2) 
        self.assertEqual(response.data['message'], 'Products successfully returned based on the given category')

    def test_list_products_by_nonexistent_category(self):
        url = reverse('https://staging.zuri.team/api/marketplace/v1/products/Nonexistent_Category/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'Category does not exist.')

    def test_list_products_with_no_products_in_category(self):
        # Create a ProductCategory with no associated products
        category = ProductCategory.objects.create(name="Empty Category")
        url = reverse('https://staging.zuri.team/api/marketplace/v1/products/Empty_Category/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 0)  
        self.assertEqual(response.data['message'], 'The Category exists, but has no products')

