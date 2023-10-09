import uuid
from decimal import Decimal
from django.utils import timezone
from M.models import Product, ProductImage, ProductCategory

# Generate seed data for the ProductCategory model
def create_product_categories():
    categories = [
        {
            "name": "Category 1",
            "parent_category_id": None,
            "status": "complete",
        },
        {
            "name": "Category 2",
            "parent_category_id": None,
            "status": "pending",
        },
        # Add more category data as needed
    ]

    for category_data in categories:
        ProductCategory.objects.create(**category_data)

# Generate seed data for the ProductImage model
def create_product_images():
    images = [
        {
            "product_id": Product.objects.get(name="Product 1"),
            "url": "image1.jpg",  # Set image URL
        },
        {
            "product_id": Product.objects.get(name="Product 2"),
            "url": "image2.jpg",  # Set image URL
        },
        # Add more image data as needed
    ]

    for image_data in images:
        ProductImage.objects.create(**image_data)

# Generate seed data for the Product model
def create_products():
    products = [
        {
            "shop_id": None,  # Set shop ID if available
            "name": "Product 1",
            "description": "Description for Product 1",
            "quantity": 100,
            "category_id": ProductCategory.objects.get(name="Category 1"),
            "price": Decimal("19.99"),
            "discount_price": Decimal("14.99"),
            "tax": Decimal("2.0"),
            "admin_status": "approved",
            "is_deleted": "active",
            "image_id": None,  # Set image ID if available
            "rating_id": None,  # Set rating ID if available
            "is_published": True,
            "currency": "USD",
        },
        {
            "shop_id": None,  # Set shop ID if available
            "name": "Product 2",
            "description": "Description for Product 2",
            "quantity": 50,
            "category_id": ProductCategory.objects.get(name="Category 2"),
            "price": Decimal("29.99"),
            "discount_price": Decimal("24.99"),
            "tax": Decimal("3.0"),
            "admin_status": "pending",
            "is_deleted": "active",
            "image_id": None,  # Set image ID if available
            "rating_id": None,  # Set rating ID if available
            "is_published": False,
            "currency": "USD",
        },
        # Add more product data as needed
    ]

    for product_data in products:
        Product.objects.create(**product_data)

# Call the functions to create seed data
create_product_categories()
create_product_images()
create_products()
