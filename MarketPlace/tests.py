from django.test import TestCase

# Create your tests here.

from rest_framework.test import APIClient
from .models import Shop, ProductCategory, Product
from django.urls import reverse
from rest_framework import status
from typing import OrderedDict


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
            # parent_category = 1,
            status="approved"
        )

        self.test_category2 = ProductCategory.objects.create(
            name="Sample Category 2",
            # parent_category = 2,
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
        url = reverse("get_products_by_categories", args=[self.test_category1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(len(response.data), None)
        for x in response.data:
            self.assertIsInstance(x, OrderedDict)
        print(response.data)

    def test_get_empty_products_list_by_category(self):
        url = reverse("get_products_by_categories", args=[self.test_category2])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
        print(response.data)

    def test_return_404_for_nonexistent_category(self):
        nonexistent_category = "NonExistentCategory"
        url = reverse("get_products_by_categories",
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
