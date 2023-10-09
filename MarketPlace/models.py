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
#     price = models.DecimalField( max_digits=20, decimal_places=2)
 
# User model from the schema
class User(models.Model):
    """Identifies the user model based on the schema"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    username = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    section_order = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    two_factor_auth = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        """defines the metadata for the product model"""
        managed = False
        db_table = "user"
        verbose_name_plural = "Users"




class Shop(models.Model):
    """defines the shop model"""
    SHOP_STATUS = (
        ('active', 'Active'),
        ('temporary', 'Temporary')
    )
    RESTRICTED = (
        ('no', 'No'),
        ('temporary', 'Temporary'),
        ('permanent', 'Permanent')
    )
    ADMIN_STATUS = (
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('suspended', 'Suspended'),
        ('blacklisted', 'Blacklisted')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    merchant_id = models.UUIDField(null=True)
    name = models.CharField(max_length=255, null=False)
    policy_confirmation = models.BooleanField(default=False)
    restricted = models.CharField(max_length=20, choices=RESTRICTED, default="no")
    admin_status = models.CharField(max_length=20, choices=ADMIN_STATUS, default="pending")
    is_deleted = models.CharField(max_length=20, choices=SHOP_STATUS, default='active')
    reviewed = models.BooleanField(default=False)
    rating = models.DecimalField( max_digits=20, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """defines the metadata for the shop model"""
        managed = False
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
    parent_category_id = models.IntegerField(default=None, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    
    class Meta:
        """defines the metadata for the product model"""
        managed = False
        db_table = "product_category"
        verbose_name_plural = "ProductCategories"


    def __str__(self) -> str:
        return self.name
# the below class is not really needed for any function on our side
# it's just added to ensure the Product class conforms with the schema

class UserProductRating(models.Model):
    """This is the user product rating, how the product is rated"""
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(null=True)
    
    
    class Meta:
        """defines the metadata for the product model"""
        managed = False
        db_table = "user_product_rating"
        verbose_name_plural = "UserProductRatings"


class Product(models.Model):
    """defines the product models"""
    ADMIN_STATUS = (
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('suspended', 'Suspended'),
        ('blacklisted', 'Blacklisted')
    )
    PRODUCT_STATUS = (
        ('active', 'Active'),
        ('temporary', 'Temporary')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    shop_id = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    quantity = models.BigIntegerField(null=False)
    category_id = models.ForeignKey('ProductCategory', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField( max_digits=20, decimal_places=2, null=False)
    discount_price = models.DecimalField( max_digits=20, decimal_places=2, null=False)
    tax = models.DecimalField( max_digits=20, decimal_places=2, null=False)
    admin_status = models.CharField(max_length=20, choices=ADMIN_STATUS, default="pending")
    is_deleted = models.CharField(max_length=20, choices=PRODUCT_STATUS, default="active")
    # image_id = models.ForeignKey('ProductImage', on_delete=models.CASCADE, null=False)
    # rating_id = models.ForeignKey('UserProductRating', on_delete=models.CASCADE, null=False)
    is_published = models.BooleanField(default=False, null=False)
    currency = models.CharField(max_length=10, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        """defines the metadata for the product model"""
        managed = False
        db_table = "product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name



    

class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    
    
    class Meta:
        """defines the metadata for the product model"""
        managed = False
        db_table = "product_image"
        verbose_name_plural = "ProductImages"


    def __str__(self) -> str:
        return self.url

class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        """defines the metadata for the product model"""
        managed = False
        db_table = "wishlist"
        verbose_name_plural = "Wishlists"

    
    


class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    
    
    class Meta:
        """defines the metadata for the product model"""
        managed = False
        db_table = "favourite"
        verbose_name_plural = "Favourites"


# THIS TABLE IS NOT ON THE GENERAL, IT SHOULD BE COMMUNICATED BEFORE 
# CREATION. 
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
