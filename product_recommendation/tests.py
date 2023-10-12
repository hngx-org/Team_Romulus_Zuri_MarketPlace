from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from MarketPlace.models import Product
from MarketPlace.serializers import ProductSerializer

class ProductRecommendationViewTest(APITestCase):
    def setUp(self):
        # Create sample products for testing
        self.product1 = Product.objects.create(
            name="Product 1",
            quantity=100,
            discount_price=50.0,
            tax=5.0,
            price=100.0
        )
        self.product2 = Product.objects.create(
            name="Product 2",
            quantity=200,
            discount_price=40.0,
            tax=6.0,
            price=90.0
        )
        self.product3 = Product.objects.create(
            name="Product 3",
            quantity=50,
            discount_price=60.0,
            tax=4.0,
            price=120.0
        )
        self.product4 = Product.objects.create(
            name="Product 4",
            quantity=150,
            discount_price=45.0,
            tax=5.5,
            price=110.0
        )

        # Create additional products to match the expected 20 in the response
        for i in range(5, 21):
            product = Product.objects.create(
                name=f"Product {i}",
                quantity=100,
                discount_price=50.0,
                tax=5.0,
                price=100.0
            )

    def test_product_recommendations(self):
        url = reverse('recommendations')  # Make sure to define the correct URL name in your URLs configuration

        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response data contains 20 products
        self.assertEqual(len(response.data), 20)

        # Check that the response data is serialized correctly
        expected_products = Product.objects.order_by('-quantity')[:20]  # You can adjust this based on your requirements
        serializer = ProductSerializer(expected_products, many=True)
        response_set = set(map(tuple, response.data))
        serializer_set = set(map(tuple, serializer.data))
        self.assertEqual(response_set, serializer_set)
    


