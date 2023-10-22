from django.test import TestCase
from django.urls import reverse
from MarketPlace.models import Product
from rest_framework import status

class ProductSearchViewTestCase(TestCase):

    def setUp(self):
        # Create a sample product
        self.product = Product.objects.create(name="Sample Product", description="This is a sample product.")
    
    # Helper function to construct the URL with query parameters
    def get_search_url(self, query):
        return f"{reverse('product_search')}?query={query}"

    def test_product_search_view_with_results(self):
        response = self.client.get(self.get_search_url('Sample'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Use DRF's status for clarity
        self.assertContains(response, "Sample Product")

    def test_product_search_view_no_results(self):
        response = self.client.get(self.get_search_url('NoMatch'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotContains(response, "Sample Product")
