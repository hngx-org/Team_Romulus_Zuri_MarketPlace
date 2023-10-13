from django.db import models
from uuid import uuid4


# class ProductView(models.Model):
#     """Represent a ProductView.
    
#     Attributes:
#         id: The id of the recently viewed product as an integer.
#         user_id: The user id of the product as a string.
#         product_id: The product id of the product as a string.
#         viewed_at: The viewd date and time of the product as a string.
#     """
#     id = models.UUIDField(primary_key=True, default=uuid4)
#     user_id = models.UUIDField()
#     product_id = models.UUIDField()
#     viewed_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         """defines the metadata for the product model"""
#         db_table = "last_viewed_product"
#         verbose_name_plural = "LastViewedProduct"

#     def __str__(self):
#         return f'{self.user_id} viewed {self.product_id} at {self.viewed_at}'

# class User(models.Model):
#     """Identifies the user model based on the schema"""
#     id = models.UUIDField(primary_key=True, default=uuid4, null=False)
#     username = models.CharField(max_length=255, null=False)
#     first_name = models.CharField(max_length=255, null=False)
#     last_name = models.CharField(max_length=255, null=False)
#     email = models.CharField(max_length=255, null=False)
#     section_order = models.CharField(max_length=200, null=True)
#     password = models.CharField(max_length=255)
#     provider = models.CharField(max_length=255)
#     is_verified = models.BooleanField(default=False)
#     two_factor_auth = models.BooleanField(default=False)
#     location = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     profile_pic = models.CharField(max_length=255)
#     refresh_token = models.CharField(max_length=255, null=False)
#     created_at = models.DateTimeField(auto_now_add=True)


# class Product(models.Model):
#     """defines the product models"""
#     ADMIN_STATUS = (
#         ('pending', 'Pending'),
#         ('reviewed', 'Reviewed'),
#         ('approved', 'Approved'),
#         ('suspended', 'Suspended'),
#         ('blacklisted', 'Blacklisted')
#     )
#     PRODUCT_STATUS = (
#         ('active', 'Active'),
#         ('temporary', 'Temporary')
#     )
#     id = models.UUIDField(primary_key=True, default=uuid4, null=False)
#     shop_id = models.BigIntegerField(null=False)
#     name = models.CharField(max_length=255, null=False)
#     description = models.CharField(max_length=255, null=False)
#     quantity = models.BigIntegerField(null=False)
#     category_id = models.CharField(max_length=255, null=False)
#     subcategory_id = models.CharField(max_length=255, null=False)
#     price = models.DecimalField( max_digits=20, decimal_places=2, null=False)
#     discount_price = models.DecimalField( max_digits=20, decimal_places=2, null=False)
#     tax = models.DecimalField( max_digits=20, decimal_places=2, null=False)
#     admin_status = models.CharField(max_length=20, choices=ADMIN_STATUS, default="pending")
#     is_deleted = models.CharField(max_length=20, choices=PRODUCT_STATUS, default="active")
#     image_id = models.CharField(max_length=255, null=False)
#     rating_id = models.BigIntegerField(null=False)
#     is_published = models.BooleanField(default=False, null=False)
#     currency = models.CharField(max_length=10, null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)