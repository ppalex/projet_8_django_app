from django.db import models

from core.models.managers.category_manager import CategoryManager


class Category(models.Model):
    """This class represents the category model (ORM)
    """

    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, unique=True)

    category_objects = CategoryManager()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name
