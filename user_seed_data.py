import uuid
from django.contrib.auth.hashers import make_password
from MarketPlace.models import User

# Generate seed data for the User model
def create_users():
    users = [
        {
            "username": "user1",
            "first_name": "John",
            "last_name": "Doe",
            "email": "user1@example.com",
            "section_order": None,
            "password": make_password("password123"),  # Hash the password
            "provider": "Google",
            "is_verified": True,
            "two_factor_auth": False,
            "location": "New York",
            "country": "USA",
            "profile_pic": "profile1.jpg",  # Set an image path
            "refresh_token": str(uuid.uuid4()),  # Generate a UUID for refresh_token
        },
        {
            "username": "user2",
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "user2@example.com",
            "section_order": None,
            "password": make_password("securepass"),  # Hash the password
            "provider": "Facebook",
            "is_verified": False,
            "two_factor_auth": True,
            "location": "San Francisco",
            "country": "USA",
            "profile_pic": "profile2.jpg",  # Set an image path
            "refresh_token": str(uuid.uuid4()),  # Generate a UUID for refresh_token
        },
        # Add more user data as needed
    ]

    for user_data in users:
        User.objects.create(**user_data)

# Call the function to create seed data
create_users()
