from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from MarketPlace.models import Product


class ProductListAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_products(self):
        Product.objects.create(name="Product1", price=10.0)
        Product.objects.create(name="Product2", price=20.0)
        response = self.client.get('https://staging.zuri.team/api/marketplace/v1/product-list/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 2)  
        

    def test_list_products_pagination(self):
        # We will Create a large number of products to test pagination
        for i in range(15):
            Product.objects.create(name=f"Product{i}", price=10.0)
        response = self.client.get('https://staging.zuri.team/api/marketplace/v1/product-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 10) 
        self.assertTrue(response.data['page_info']['next'])
        

    def test_list_products_no_data(self):
        response = self.client.get('https://staging.zuri.team/api/marketplace/v1/product-list/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 0)  
        

    

