from django.db import models

from core.models.managers.store_manager import StoreManager


class Store(models.Model):
    """This class represents the store model (ORM)
    """
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=255, unique=True)

    store_objects = StoreManager()

    def __str__(self):
        return self.store_name
