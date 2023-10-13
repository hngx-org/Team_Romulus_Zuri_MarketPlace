from django.test import TestCase
from rest_framework.test import APIClient
from MarketPlace.models import ProductCategory, ProductSubCategory
from django.urls import reverse
from rest_framework import status

# Create your tests here.




class CategoryNameViewTest(TestCase):
    # databases='__all__'
    def setUp(self):
        self.client = APIClient()
        
        self.category1 = ProductCategory.objects.create(
            name="Sample 1",
        )
        
        self.category2 = ProductCategory.objects.create(
            name="Sample 2",
        )
        
        self.category3 = ProductCategory.objects.create(
            name="Sample 3",
        )
        
        self.subcategory1 = ProductSubCategory.objects.create(
            name="Sample sub 1",
            parent_category=self.category1
        )
        
        self.subcategory2 = ProductSubCategory.objects.create(
            name="Sample sub 2",
            parent_category=self.category3
        )
        
        self.subcategory3 = ProductSubCategory.objects.create(
            name="Sample sub 3",
            parent_category=self.category2
        )
        
        self.subcategory4 = ProductSubCategory.objects.create(
            name="Sample sub 4",
            parent_category=self.category3
        )
        
        self.subcategory5 = ProductSubCategory.objects.create(
            name="Sample sub 5",
            parent_category=self.category1
        )
        
        self.subcategory6 = ProductSubCategory.objects.create(
            name="Sample sub 6",
            parent_category=self.category2
        )
        
        self.subcategory7 = ProductSubCategory.objects.create(
            name="Sample sub 7",
            parent_category=self.category3
        )
        
        self.subcategory8 = ProductSubCategory.objects.create(
            name="Sample sub 8",
            parent_category=self.category3
        )
        
        self.subcategory9 = ProductSubCategory.objects.create(
            name="Sample sub 9",
            parent_category=self.category2
        )
        
        self.subcategory10 = ProductSubCategory.objects.create(
            name="Sample sub 10",
            parent_category=self.category1
        )
        
    def test_retrieve_category_subcategory(self):
        from typing import OrderedDict
        
        url = reverse("category_name")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_response = {
            'categories': [
                {'name': 'Sample 1', 'subcategories': [
                    OrderedDict([('name', 'Sample sub 1')]),
                    OrderedDict([('name', 'Sample sub 5')]),
                    OrderedDict([('name', 'Sample sub 10')])
                    ]
                },
                {'name': 'Sample 2', 'subcategories': [
                    OrderedDict([('name', 'Sample sub 3')]),
                    OrderedDict([('name', 'Sample sub 6')]),
                    OrderedDict([('name', 'Sample sub 9')])
                    ]
                },
                {'name': 'Sample 3', 'subcategories': [
                    OrderedDict([('name', 'Sample sub 2')]),
                    OrderedDict([('name', 'Sample sub 4')]),
                    OrderedDict([('name', 'Sample sub 7')]),
                    OrderedDict([('name', 'Sample sub 8')])
                    ]
                }
                ]
            }
        self.assertEqual(expected_response, response.data)
        print(response.data)
        
    def tearDown(self):
        self.category1.delete()
        self.category2.delete()
        self.category3.delete()
        self.subcategory1.delete()
        self.subcategory2.delete()
        self.subcategory3.delete()
        self.subcategory4.delete()
        self.subcategory5.delete()
        self.subcategory6.delete()
        self.subcategory7.delete()
        self.subcategory8.delete()
        self.subcategory9.delete()
        self.subcategory10.delete()