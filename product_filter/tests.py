from django.test import TestCase
from rest_framework.test import APIClient
from MarketPlace.models import ProductCategory, Product
from django.urls import reverse
from rest_framework import status


class TestFilterProductView(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.category1 = ProductCategory.objects.create(name='Electronics')
        cls.category2 = ProductCategory.objects.create(name='Online_Tutoring')
        cls.product1 = Product.objects.create(
            name='product1',
            description='Product1 description',
            quantity=10,
            category=cls.category1,
            price=1000.00,
            discount_price=900.00,
            tax=50.00,
            is_published=True,
            currency='Naira',
            is_deleted='active',
            admin_status='approved'
        )
        cls.product2 = Product.objects.create(
            name='product2',
            description='Product2 description',
            quantity=15,
            category=cls.category1,
            price=1500.00,
            discount_price=1350.00,
            tax=75.00,
            is_published=True,
            currency='Naira',
            is_deleted='active',
            admin_status='approved'
        )
        cls.product3 = Product.objects.create(
            name='product3',
            description='Product3 description',
            quantity=25,
            category=cls.category2,
            price=1300.00,
            discount_price=1250.00,
            tax=65.00,
            is_published=True,
            currency='Naira',
            is_deleted='active',
            admin_status='approved'
        )

    def test_filter_products(self):
        # To create a query parameter with keywords, category and discount
        query_params = {
            'category': self.category2.id,
            'keywords': 'device',
            'discount': '1300.00'  # filter products with discount <= 1300
        }

        url = reverse('filter_products')
        response = self.client.get(url, data=query_params)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        # Check if the expected number of products is returned
        self.assertEqual(len(response_data['data']['products']), 1)

        # Check if the returned product matches the filter criteria
        filtered_product = response_data['data']['products'][0]
        self.assertTrue('device' in filtered_product['name'].lower() or 'device' in filtered_product['description'].lower())
        self.assertEqual(filtered_product['category_id'], query_params['category'])
        self.assertLessEqual(float(filtered_product['discount_price']), float(query_params['discount']))

    def tearDown(self):
        self.category1.delete()
        self.category2.delete()
        self.product1.delete()
        self.product2.delete()
        self.product3.delete()
# ----------------------------------------------------------------------------------------------------------#      