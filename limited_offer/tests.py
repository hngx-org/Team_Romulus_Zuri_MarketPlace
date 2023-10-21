from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from MarketPlace.models import Product
from all_products.serializers import AllProductSerializer as ProductSerializer

class LimitedOfferListViewTest(APITestCase):
    def setUp(self):
        # Create some sample products with discounts for testing
        self.product1 = Product.objects.create(
            name="Product 1",
            discount_price=10.0,
            is_deleted='active',
            admin_status='approved'
        )
        self.product2 = Product.objects.create(
            name="Product 2",
            discount_price=20.0,
            is_deleted='active',
            admin_status='approved'
        )
        self.url = reverse('limited-offer-list')

    def test_list_with_discounts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Check if both products with discounts are returned

    def test_list_no_discounts(self):
        # Make sure there are no products with discounts
        self.product1.discount_price = 0.0
        self.product1.save()
        self.product2.discount_price = 0.0
        self.product2.save()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'No discounts found.')

    def test_list_exception_handling(self):
        # Simulate an exception during serialization
        Product.objects.all().delete()  # Delete all products to cause an exception
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
