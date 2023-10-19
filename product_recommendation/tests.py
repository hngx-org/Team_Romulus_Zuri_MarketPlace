from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from MarketPlace.models import Product, ProductCategory
from MarketPlace.serializers import ProductSerializer
from rest_framework.test import APIClient
from django.test import TestCase
import uuid

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
    

class TestSimilarProductView(TestCase):
    def setUp(self):
        self.client = APIClient()

        # To create sample categories
        self.category1 = ProductCategory.objects.create(name='Electronics',)
        self.category2 = ProductCategory.objects.create(name='Online_Tutoring')

        # To create sample products
        self.product1 = Product.objects.create(id=uuid.uuid4(), name='product1',
                                               description='Product1 description', quantity=10,
                                               category=self.category1, price=1000.00, discount_price=900.00,
                                               tax=50.00, is_published=True, currency='Naira',
                                               is_deleted='active', admin_status='approved')
        self.product2 = Product.objects.create(id=uuid.uuid4(), name='product2',
                                               description='Product2 description device', quantity=15,
                                               category=self.category1, price=1500.00, discount_price=1350.00,
                                               tax=75.00, is_published=True, currency='Naira',
                                               is_deleted='active', admin_status='approved')
        self.product3 = Product.objects.create(id=uuid.uuid4(), name='product3',
                                               description='Product3 description', quantity=25,
                                               category=self.category1, price=1300.00, discount_price=1250.00,
                                               tax=65.00, is_published=True, currency='Naira',
                                               is_deleted='active', admin_status='approved')
        self.product4 = Product.objects.create(id=uuid.uuid4(), name='product4',
                                               description='Product4 description', quantity=45,
                                               category=self.category2, price=1300.00, discount_price=1250.00,
                                               tax=65.00, is_published=True, currency='Naira',
                                               is_deleted='active', admin_status='approved')

    def test_get_similar_products(self):
        # GET request to SimilarProductView endpoint
        url = reverse('similar-products', kwargs={'product_id': self.product1.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # print(response.data)

        # To confirm that the products returned are similar products
        self.assertEqual(len(response.data['response_data']["data"]["similar_products"]), 2)

        # To confirm that the 'un-similar' product is not among the returned products
        json_response = response.json()
        product4 = ProductSerializer(self.product4)
        self.assertNotEqual(json_response['response_data']["data"]["similar_products"][-1], product4.data)
        print(json_response['response_data']["data"])  # print(json_response['products'][-1])

        # To confirm the products returned have the same category
        # for product in response.data['products']:
        for product in response.data['response_data']["data"]["similar_products"]:
            self.assertEqual(product['category_id'], self.category1.id)
        # self.assertTrue(response['products'][:], self.category1.id)

    def tearDown(self):
        self.category1.delete()
        self.category2.delete()
        self.product1.delete()
        self.product2.delete()
        self.product3.delete()
        self.product4.delete()


