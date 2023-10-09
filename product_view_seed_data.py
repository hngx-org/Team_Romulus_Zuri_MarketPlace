import uuid
from django.utils import timezone
from product_view.models import ProductView

# Generate seed data for the ProductView model
def create_product_views():
    product_views = [
        {
            "user_id": str(uuid.uuid4()),  # Generate a random UUID for user_id
            "product_id": str(uuid.uuid4()),  # Generate a random UUID for product_id
            "viewed_at": timezone.now() - timezone.timedelta(days=10),  # Set a date in the past
        },
        {
            "user_id": str(uuid.uuid4()),
            "product_id": str(uuid.uuid4()),
            "viewed_at": timezone.now() - timezone.timedelta(days=5),  # Set a date in the past
        },
        # Add more product view data as needed
    ]

    for product_view_data in product_views:
        ProductView.objects.create(**product_view_data)

# Call the function to create seed data
create_product_views()
