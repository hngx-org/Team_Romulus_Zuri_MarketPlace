from django.test import TestCase
from rest_framework.test import APIClient
from MarketPlace.models import Shop, ProductCategory, ProductSubCategory, Product
from django.urls import reverse
from rest_framework import status
import uuid
# from .serializers import ProductSerializer


class TestFilterProductView(TestCase):
    def setUp(self):
        self.client = APIClient()
        # To create sample categories
        self.category1 = ProductCategory.objects.create(name='Electronics')
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
                                               category=self.category2, price=1300.00, discount_price=1250.00,
                                               tax=65.00, is_published=True, currency='Naira',
                                               is_deleted='active', admin_status='approved')

    def test_filter_products(self):
        # To create a query parameter with keywords, category and discount
        query_params = {
            'category': self.category2.id,
            'keywords': 'device',
            'discount': '1300.00'  # filter products with discount <= 1300
        }

        # GET request to FilterProductView endpoint with query parameters as filters
        url = reverse('filter_products')
        response = self.client.get(url, data={'ordering': 'name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

        # To verify that the products returned match at least one of the filter criteria(keywords):
        filtered_products = response.json()
        for product in filtered_products['response_data']["data"]["products"]:
            self.assertTrue(
                any(q.lower() in product['name'].lower() or product['description'].lower() for q in query_params['keywords'].split(','))
            )

        # To verify that the products returned matches at least one of the filter criteria(category):
        # for product in filtered_products['products']:
        for product in filtered_products['response_data']["data"]["products"]:
            if product['category_id'] == query_params['category']:
                self.assertTrue(product['category_id'], query_params['category'])

        # for product in filtered_products['products']:
        for product in filtered_products['response_data']["data"]["products"]:
            if product['discount_price'] <= query_params['discount']:
                self.assertLessEqual(product['discount_price'], query_params['discount'])
                self.assertEqual(len(response.data['products']), 3)

    def tearDown(self):
        self.category1.delete()
        self.category2.delete()
        self.product1.delete()
        self.product2.delete()
# ----------------------------------------------------------------------------------------------------------#
