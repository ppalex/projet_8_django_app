from django.db import models

from django.apps import apps

from django.db import IntegrityError
import logging

class ProductManager(models.Manager):
    
    def create_product(self, barcode, product_name, nutriscore_grade, product_description, off_url):
        
        product_model = apps.get_model('core', 'Product')
        
        try:
            product = product_model.product_objects.create(barcode=barcode,
                                    product_name=product_name,
                                    nutriscore_grade=nutriscore_grade,
                                    product_description=product_description,
                                    off_url=off_url)

            return product

        except IntegrityError:
                logging.error("Integrity violation")
                return None
                               
        


    def insert_product_db(self, product_list):
        
        category_model = apps.get_model('core', 'Category')
        store_model = apps.get_model('core', 'Store')
        
        for element in product_list:
            product = self.create_product(element.barcode,
                                            element.product_name,
                                            element.nutriscore_grade,
                                            element.description,
                                            element.off_url)
            if product is not None:
                product.save()
                
                categories = [category_model.objects.create(category_name=category) for category in element.categories]
                stores = [store_model.objects.create(store_name=store) for store in element.stores]
                product.categories.add(*categories)
                product.stores.add(*stores)
    