from django.db import models

class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=255)

    def __str__(self):
        return self.store_name