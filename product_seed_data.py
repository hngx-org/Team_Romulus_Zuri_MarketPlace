import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")  # Replace with your project's settings module
django.setup()

from MarketPlace.models import Product, ProductImage  # Replace 'myapp' with your actual app name

# Create Product instances
product_instance_1 = Product.objects.create(
    name="Product 1",
    description="Description for Product 1",
    quantity=10,
    price=50.00,
    discount_price=45.00,
    tax=5.00,
    admin_status="approved",
    is_deleted="active",
    currency="USD",
)

product_instance_2 = Product.objects.create(
    name="Product 2",
    description="Description for Product 2",
    quantity=20,
    price=60.00,
    discount_price=55.00,
    tax=5.00,
    admin_status="approved",
    is_deleted="active",
    currency="USD",
)

# Now, you can use product_instance_1 and product_instance_2 in your seed data script.


# Define seed data for ProductImages
product_images = [
    {
        "product_id": product_instance_1.id,
        "url": "https://example.com/image1.jpg",
    },
    {
        "product_id": product_instance_2.id,
        "url": "https://example.com/image2.jpg",
    },
    # Add more product image data as needed
]

# Create ProductImage instances in the database
for image_data in product_images:
    ProductImage.objects.create(
        product_id=image_data["product_id"],
        url=image_data["url"]
    )

print("Seed data for ProductImages has been inserted into the database.")
