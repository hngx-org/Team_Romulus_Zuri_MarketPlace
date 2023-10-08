from django.db import models
import uuid


# Create your models here.

# test user profile for making recommendation
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10) 


# test product table for testing the recommendation logic
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     category = models.CharField(max_length=50)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
 


class Shop(models.Model):
    """defines the shop model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    merchant_id = models.UUIDField(null=True)
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=False)
    policy_confirmation = models.BooleanField(default=False)
    restricted = models.CharField(max_length=10, default="no")
    admin_status = models.CharField(max_length=10, default="pending")
    reviewed = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """defines the metadata for the shop model"""
        db_table = "shop"
        verbose_name_plural = "Shops"

    def __str__(self):
        return self.name

class ProductCategory(models.Model):    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('complete', 'Complete'),
        ('failed', 'Failed'),
    ]#defining the valid options for status field

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    parent_category_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    """defines the product models"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    user_id = models.UUIDField(null=True)
    shop_id = models.ForeignKey('Shop', on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    quantity = models.BigIntegerField(null=False)
    category = models.ForeignKey('ProductCategory', on_delete=models.SET_NULL, null=True)

    image_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    admin_status = models.CharField(max_length=10, default="pending")
    rating_id = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False, null=False)
    currency = models.CharField(max_length=10, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        """defines the metadata for the product model"""
        db_table = "product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name



    

class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.UUIDField(unique=True)
    url = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.url

class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField()
    product_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField(null=False)
    product_id = models.UUIDField(null=False)


# table for implementing the recommendation login
class UserProductInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=10)  # e.g., "viewed," "purchased"
    timestamp = models.DateTimeField(auto_now_add=True)

class WishListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist Item"
