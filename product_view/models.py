from django.db import models
from uuid import uuid4

class ProductView(models.Model):
    """Represent a ProductView.
    
    Attributes:
        id: The id of the recently viewed product as an integer.
        user_id: The user id of the product as a string.
        product_id: The product id of the product as a string.
        viewed_at: The viewd date and time of the product as a string.
    """
    id = models.UUIDField(primary_key=True, default=uuid4)
    user_id = models.UUIDField()
    product_id = models.UUIDField()
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """defines the metadata for the product model"""
        managed = False
        db_table = "last_viewed_product"
        verbose_name_plural = "LastViewedProduct"

    def __str__(self):
        return f'{self.user_id} viewed {self.product_id} at {self.viewed_at}'
