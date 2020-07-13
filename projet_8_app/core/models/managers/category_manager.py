from django.db import models

from django.apps import apps

from django.db import IntegrityError
import logging

class ProductManager(models.Manager):
    
    def create_category(self):
        
        category_model = apps.get_model('core', 'Category')
        
        try:
            category = category_model.product_objects.create()

            return category

        except IntegrityError:
                logging.error("Integrity violation")
                return None


    def insert_categories_db(self, product):
        pass