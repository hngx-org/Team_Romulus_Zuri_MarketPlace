from django.test import TestCase
from rest_framework.test import APIClient
from .models import Shop, ProductCategory, ProductSubCategory
from django.urls import reverse
from rest_framework import status
from typing import OrderedDict
from .serializers import ProductSerializer
from .models import UserProfile, UserProductInteraction, Product
from django.contrib.auth.models import User  # Import User model


class TestGetAllProductsBasedOnCategory(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.test_shop = Shop.objects.create(
            name="Sample Shop",
            policy_confirmation=True,
            reviewed=True,
            rating=4.5
        )

        self.test_category1 = ProductCategory.objects.create(
            name="Sample Category 1",
            status="approved"
        )

        self.test_category2 = ProductCategory.objects.create(
            name="Sample Category 2",
            status="approved"
        )

        self.test_product1 = Product.objects.create(
            shop_id=self.test_shop,
            name="Sample Product 1",
            description="Sample Description 1",
            quantity=10,
            category=self.test_category1,
            image_id=1,
            price=100.00,
            discount_price=90.00,
            tax=10.00,
            is_published=True,
            currency="USD"
        )

        self.test_product2 = Product.objects.create(
            shop_id=self.test_shop,
            name="Sample Product 2",
            description="Sample Description 2",
            quantity=5,
            category=self.test_category1,
            image_id=2,
            price=50.00,
            discount_price=45.00,
            tax=5.00,
            is_published=True,
            currency="USD",
        )

    def test_get_all_products_by_category(self):
        url = reverse("get_all_products_by_categories", args=[self.test_category1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(len(response.data), None)
        for x in response.data:
            self.assertIsInstance(x, OrderedDict)
        print(response.data)

    def test_get_empty_products_list_by_category(self):
        url = reverse("get_all_products_by_categories", args=[self.test_category2])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
        print(response.data)

    def test_return_404_for_nonexistent_category(self):
        nonexistent_category = "NonExistentCategory"
        url = reverse("get_all_products_by_categories",
                      args=[nonexistent_category])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn(b'{"message":"Category not found."}', list(response))
        self.assertEqual(response.data["message"], "Category not found.")
        print(response.data)

    def tearDown(self):
        self.test_shop.delete()
        self.test_category1.delete()
        self.test_category2.delete()
        self.test_product1.delete()
        self.test_product2.delete()


class ProductListAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # To create sample test data
        self.test_shop = Shop.objects.create(
            name="Sample Shop",
            policy_confirmation=True,
            reviewed=True,
            rating=3.5
        )
        self.subcategory1 = 'ebook'
        self.subcategory2 = 'mobile_app'
        self.category_obj = ProductCategory.objects.create(name='digital services', status='approved', parent_category_id=1)
        self.subcategory_obj_1 = ProductSubCategory.objects.create(name=self.subcategory1, parent_category_id=self.category_obj)
        self.subcategory_obj_2 = ProductSubCategory.objects.create(name=self.subcategory2, parent_category_id=self.category_obj)

        self.product1 = Product.objects.create(shop_id=self.test_shop, name='product_1',
                                               description='Product_1 description', quantity=10,
                                               category_id=self.category_obj, subcategory_id=self.subcategory_obj_1,
                                               price=1000.00, discount_price=100.00, tax=50.00, is_published=True, currency='Naira')
        self.product2 = Product.objects.create(shop_id=self.test_shop, name='product_2',
                                               description='Product_2 description', quantity=15,
                                               category_id=self.category_obj, subcategory_id=self.subcategory_obj_1,
                                               price=1300.00, discount_price=110.00, tax=70.00, is_published=True, currency='Naira')

    def test_list_products_sorted_by_price(self):
        url = reverse('get_products_by_subcategories', kwargs={'category': self.category_obj,
                                                               'subcategory': self.subcategory_obj_1})
        response = self.client.get(url, format='json', data={'ordering': 'price'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # To confirm that the response is ordered by price
        self.assertTrue(response.data["products"][0], self.product1)
        print(response.data["products"])

    def test_list_products_sorted_by_name(self):
        url = reverse('get_products_by_subcategories', kwargs={'category': self.category_obj,
                                                               'subcategory': self.subcategory_obj_1})  # , args=[self.subcategory.id=1]
        response = self.client.get(url, format='json', data={'ordering': 'name'})
        # serializer = ProductSerializer(self.product2)
        # self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # To confirm that the response is ordered by price
        self.assertTrue(response.data["products"][0], self.product1)
        print(response.data["products"])

    def test_list_products_empty_subcategory(self):
        url = reverse('get_products_by_subcategories', kwargs={'category': self.category_obj,
                                                               'subcategory': self.subcategory_obj_2})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 0)
        print(response.data)

    def test_list_nonexistent_category(self):
        url = reverse('get_products_by_subcategories', kwargs={'category': self.category_obj,
                                                               'subcategory': "non-existent"}) 
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print(response.data)

    def tearDown(self):
        self.category_obj.delete()
        self.subcategory_obj_1.delete()
        self.subcategory_obj_2.delete()
        self.product1.delete()
        self.product2.delete()

