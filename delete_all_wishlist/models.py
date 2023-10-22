from django.contrib.auth.models import User
from django.db import models

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delete_all_wishlist_set')
    # ... other fields ...
