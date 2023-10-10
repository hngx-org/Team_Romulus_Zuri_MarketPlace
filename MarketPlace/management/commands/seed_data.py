# Import necessary modules at the beginning of the file

import random
import uuid
from django.core.management.base import BaseCommand
from MarketPlace.models import Shop, Product, ProductCategory, ProductImage, Favorites, Wishlist, User

class Command(BaseCommand):
    help = 'Seed database with testing data'

    def handle(self, *args, **options):
        # Seed ProductCategory instances
        import django
        django.setup()
        from MarketPlace.models import Shop, Product, ProductCategory, ProductImage, Favorites, Wishlist, User

        # All other seed datas
        categories = ['Electronics', 'Clothing', 'Books', 'Furniture', 'Toys']
        main_categories = []

        for category_name in categories:
            main_category = ProductCategory.objects.create(name=category_name, parent_category_id=True)
            main_categories.append(main_category)
        
        # Create subcategories for each of the main categories
        for main_category in main_categories:
            for i in range(1, 5):
                sub_category_name = f'{main_category.name}{i}'
                ProductCategory.objects.create(
                    name=sub_category_name,
                    parent_category_id=main_category.id
                )

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

            # Choose a random ProductImage instance
            # product_image = random.choice(ProductImage.objects.all())

            Product.objects.create(
                id=uuid.uuid4(),
                shop_id=shop,
                name=f'Product {random.randint(1, 100)}',
                description=f'Description for Product {random.randint(1, 100)}',
                quantity=random.randint(1, 100),
                category_id=category,
                # image_id=product_image,  # Assign the ProductImage instance
                price=random.uniform(10.0, 100.0),
                discount_price=random.uniform(5.0, 50.0),
                tax=random.uniform(1.0, 10.0),
                admin_status='approved',
                # rating_id=random.randint(1, 5),
                is_published=True,
                currency='USD',
            )


        # Seed ProductImage instances
        if ProductImage.objects.exists():  # Check if there are any ProductImage instances
            for product in Product.objects.all():
                # image_file_path = f'C:/Users/Admin/Documents/Team_Romulus_Zuri_MarketPlace-1/images/{random.randint(1, 10)}.jpg'
                # product_image = random.choice(ProductImage.objects.all())  # Choose a random ProductImage instance
                ProductImage.objects.create(
                    product_id=product.id,
                    url='https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg'  # Use the URL from the existing ProductImage
                )

        # create users
        for _ in range(5):
            User.objects.create(
                username=f'Newuser{random.randint(1, 1000)}',
                first_name=f'Firstname{random.randint(1, 1000)}',
                last_name=f'Lastname{random.randint(1, 1000)}',
                email=f'email{random.randint(1, 1000)}@gmail.com',
                password=f'password{random.randint(1, 1000)}',
                provider=f'provider{random.randint(1, 1000)}',
                location=f'location{random.randint(1, 1000)}',
                country=f'country{random.randint(1, 1000)}',
                profile_pic='https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg',
                refresh_token=f'token{random.randint(1, 1000)}'

                )


        # 
        
        # Seed Wishlist instances
        for _ in range(5):
            user = random.choice(User.objects.all())  # Choose a random User instance
            product = random.choice(Product.objects.all())  # Choose a random Product instance

            Wishlist.objects.create(
                user_id=user,  # Assign the User instance
                product_id=product,
            )

        # Seed Favorites instances
        for _ in range(3):
            user = random.choice(User.objects.all())  # Choose a random User instance
            product = random.choice(Product.objects.all())  # Choose a random Product instance

            Favorites.objects.create(
                user_id=user,  # Assign the User instance
                product_id=product,
            )

        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database with testing data.'))


# import random
# import uuid
# from django.core.management.base import BaseCommand
# from MarketPlace.models import Shop, Product, ProductCategory, ProductImage, Favorites, Wishlist

# class Command(BaseCommand):
#     help = 'Seed database with testing data'

#     def handle(self, *args, **options):
#         # Seed ProductCategory instances
#         import django
#         django.setup()
#         from MarketPlace.models import Shop, Product, ProductCategory, ProductImage, Favorites, Wishlist

#         # All other seed datas
#         categories = ['Electronics', 'Clothing', 'Books', 'Furniture', 'Toys']
#         main_categories = []

#         for category_name in categories:
#             main_category = ProductCategory.objects.create(name=category_name, parent_category_id=True)
#             main_categories.append(main_category)
        
#         # Create subcategories for each of the main categories
#         for main_category in main_categories:
#             for i in range(1, 5):
#                 sub_category_name = f'{main_category.name}{i}'
#                 ProductCategory.objects.create(
#                     name=sub_category_name,
#                     parent_category_id=main_category.id
#                     )

#         # Seed Shop instances
#         for _ in range(5):
#             Shop.objects.create(
#                 id=uuid.uuid4(),
#                 merchant_id=uuid.uuid4(),
#                 name=f'Shop {random.randint(1, 100)}',
#                 policy_confirmation=True,
#                 reviewed=True,
#                 rating=random.uniform(3.0, 5.0),
#             )

#         # # Seed Product instances
#         # for _ in range(10):
#         #     shop = random.choice(Shop.objects.all())
#         #     category = random.choice(ProductCategory.objects.all())
#         #     Product.objects.create(
#         #         id=uuid.uuid4(),
#         #         shop_id=shop,
#         #         name=f'Product {random.randint(1, 100)}',
#         #         description=f'Description for Product {random.randint(1, 100)}',
#         #         quantity=random.randint(1, 100),
#         #         category=category,
#         #         image_id=random.randint(1, 10),
#         #         price=random.uniform(10.0, 100.0),
#         #         discount_price=random.uniform(5.0, 50.0),
#         #         tax=random.uniform(1.0, 10.0),
#         #         admin_status='approved',
#         #         rating_id=random.randint(1, 5),
#         #         is_published=True,
#         #         currency='USD',
#         #     )

#         # Seed Product instances
#         for _ in range(10):
#             shop = random.choice(Shop.objects.all())
#             category = random.choice(ProductCategory.objects.all())
#             product_image = random.choice(ProductImage.objects.all())  # Choose a random ProductImage instance
            
#             Product.objects.create(
#                 id=uuid.uuid4(),
#                 shop_id=shop,
#                 name=f'Product {random.randint(1, 100)}',
#                 description=f'Description for Product {random.randint(1, 100)}',
#                 quantity=random.randint(1, 100),
#                 category=category,
#                 image_id=product_image,  # Assign the ProductImage instance here
#                 price=random.uniform(10.0, 100.0),
#                 discount_price=random.uniform(5.0, 50.0),
#                 tax=random.uniform(1.0, 10.0),
#                 admin_status='approved',
#                 rating_id=random.randint(1, 5),
#                 is_published=True,
#                 currency='USD',
#             )


#         # Seed ProductImage instances
#         for product in Product.objects.all():
#             ProductImage.objects.create(
#                 product_id=product.id,
#                 url=f'/path/to/product_images/{random.randint(1, 10)}.jpg',
#             )

#         # Seed Wishlist instances
#         for _ in range(5):
#             Wishlist.objects.create(
#                 user_id=uuid.uuid4(),
#                 product_id=uuid.uuid4()
#             )

#         # Seed Favorites instances
#         for _ in range(3):
#             Favorites.objects.create(
#                 user_id=uuid.uuid4(),
#                 product_id=uuid.uuid4()
#             )

#         self.stdout.write(self.style.SUCCESS('Successfully seeded database with testing data.'))
