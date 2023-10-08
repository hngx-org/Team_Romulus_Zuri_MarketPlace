import uuid
import random
from django.core.management.base import BaseCommand
from MarketPlace.models import Shop, Product, ProductCategory, ProductImage

class Command(BaseCommand):
    help = 'Seed database with testing data'

    def handle(self, *args, **options):
        # Seed ProductCategory instances
        categories = ['Electronics', 'Clothing', 'Books', 'Furniture', 'Toys']
        for category_name in categories:
            ProductCategory.objects.create(name=category_name)

        # Seed Shop instances
        for _ in range(5):
            Shop.objects.create(
                id=uuid.uuid4(),
                merchant_id=uuid.uuid4(),
                name=f'Shop {random.randint(1, 100)}',
                policy_confirmation=True,
                reviewed=True,
                rating=random.uniform(3.0, 5.0),
            )

        # Seed Product instances
        for _ in range(10):
            shop = random.choice(Shop.objects.all())
            category = random.choice(ProductCategory.objects.all())
            Product.objects.create(
                id=uuid.uuid4(),
                shop_id=shop,
                name=f'Product {random.randint(1, 100)}',
                description=f'Description for Product {random.randint(1, 100)}',
                quantity=random.randint(1, 100),
                category=category,
                image_id=random.randint(1, 10),
                price=random.uniform(10.0, 100.0),
                discount_price=random.uniform(5.0, 50.0),
                tax=random.uniform(1.0, 10.0),
                admin_status='approved',
                rating_id=random.randint(1, 5),
                is_published=True,
                currency='USD',
            )

        # Seed ProductImage instances
        for product in Product.objects.all():
            ProductImage.objects.create(
                product_id=product.id,
                url=f'/path/to/product_images/{random.randint(1, 10)}.jpg',
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with testing data.'))
