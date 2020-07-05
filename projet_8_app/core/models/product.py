from django.db import models

from .category import Category
from .store import Store

class Product(models.Model):
    
    barcode = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    nutriscore_grade = models.CharField(max_length=4)
    product_description = models.TextField()
    off_url = models.CharField(max_length=255)
    
    categories = models.ManyToManyField(Category)
    stores = models.ManyToManyField(Store)
    substitutes = models.ManyToManyField("self")