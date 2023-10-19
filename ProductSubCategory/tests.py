from django.test import TestCase
from rest_framework.test import APIClient
from MarketPlace.models import Shop, Product, ProductCategory, ProductSubCategory
from django.urls import reverse
from rest_framework import status
from typing import OrderedDict
import uuid
# from .serializers import ProductSerializer
# from .models import UserProfile, UserProductInteraction, Product
# from django.contrib.auth.models import User  # Import User model
# Create your tests here.


class ProductListAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # To create sample test data
        # self.test_shop = Shop.objects.create(
        #     name="Sample Shop",
        #     policy_confirmation=True,
        #     reviewed=True,
        #     rating=3.50
        # )
        self.subcategory1 = 'ebook'
        self.subcategory2 = 'mobile_app'
        self.category_obj = ProductCategory.objects.create(name='digital_services')
        self.category_obj_2 = ProductCategory.objects.create(name='tech_firms')
        self.subcategory_obj_1 = ProductSubCategory.objects.create(name=self.subcategory1, parent_category=self.category_obj)
        self.subcategory_obj_2 = ProductSubCategory.objects.create(name=self.subcategory2, parent_category=self.category_obj)

        self.product1 = Product.objects.create(id=uuid.uuid4(), name='product_1',
                                               description='Product_1 description', quantity=10,
                                               category=self.category_obj, price=1000.00, discount_price=50.00,
                                               tax=25.00, is_published=True, currency='Naira',
                                               is_deleted='active', admin_status='approved')
        self.product2 = Product.objects.create(id=uuid.uuid4(), name='product_2',
                                               description='Product_2 description', quantity=15,
                                               category=self.category_obj, price=1300.00, discount_price=110.00,
                                               tax=70.00, is_published=True, currency='Naira',
                                               is_deleted='active', admin_status='approved')

    def test_list_products_sorted_by_price(self):
        url = reverse('product-sub-category', kwargs={'category': self.category_obj,
                                                      'subcategory': self.subcategory_obj_1})
        response = self.client.get(url, format='json', data={'ordering': 'price'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # To confirm that the response is ordered by price
        self.assertTrue(response.data["response"]["data"][0], self.product1)
        print(response.data["response"])
        print("******************************************************************")
        print(response.data["response"]["data"][0])

    def test_list_products_sorted_by_name(self):
        url = reverse('product-sub-category', kwargs={'category': self.category_obj,
                                                      'subcategory': self.subcategory_obj_1})  # , args=[self.subcategory.id=1]
        response = self.client.get(url, format='json', data={'ordering': 'name'})
        # serializer = ProductSerializer(self.product2)
        # self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # To confirm that the response is ordered by name
        self.assertTrue(response.data["products"][0], self.product1)
        print(response.data["products"])

    def test_list_products_empty_subcategory(self):
        url = reverse('product-sub-category', kwargs={'category': self.category_obj, 'subcategory': self.subcategory_obj_2})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 0)
        print(response.data)

    def test_list_nonexistent_category(self):
        url = reverse('product-sub-category', kwargs={'category': 'non-existent', 'subcategory': "non-existent"})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print(response.data)

    def tearDown(self):
        self.category_obj.delete()
        self.category_obj_2.delete()
        self.subcategory_obj_1.delete()
        self.subcategory_obj_2.delete()
        self.product1.delete()
        self.product2.delete()

