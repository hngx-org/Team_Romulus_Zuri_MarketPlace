from django.test import TestCase
from django.urls import reverse
from MarketPlace.models import Product
from django.contrib.auth.models import User

class ProductSearchViewTestCase(TestCase):

    def setUp(self):
        # Create a sample product
        self.product = Product.objects.create(name="Sample Product", description="This is a sample product.")

    def test_product_search_view_with_results(self):
        response = self.client.get(reverse('product_search') + '?query=Sample')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Product")

    def test_product_search_view_no_results(self):
        response = self.client.get(reverse('product_search') + '?query=NoMatch')
        self.assertEqual(response.status_code, 200)
        # Depending on how your view handles it, you can check for an appropriate response
        # For now, I'll just check that the sample product doesn't appear in the response.
        self.assertNotContains(response, "Sample Product")
        
# You can add more tests related to different functionalities of your product_retrieval app.
