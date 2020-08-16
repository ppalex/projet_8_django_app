import logging
from random import randint

from django.apps import apps
from django.db import IntegrityError, models

from core.models.managers.store_manager import StoreManager
from core.models.managers.category_manager import CategoryManager


class ProductManager(models.Manager):
    
    def create_product(self, barcode, product_name, 
                            nutriscore_grade, product_description,
                            off_url, image_url):
        
        product_model = apps.get_model('core', 'Product')
        
        try:
            product = product_model.product_objects.create(barcode=barcode,
                                    product_name=product_name,
                                    nutriscore_grade=nutriscore_grade,
                                    product_description=product_description,
                                    off_url=off_url,
                                    image_url=image_url)

            return product

        except IntegrityError:
                logging.error("Integrity violation")
                return None                            
 
    def insert_product_db(self, product_list):     
        
        for element in product_list:

            product = self.create_product(element.barcode,
                                            element.product_name,
                                            element.nutriscore_grade,
                                            element.description,
                                            element.off_url,
                                            element.image_url)
            if product is not None:                
                stores = []
                product.save()      
               
                categories = CategoryManager().get_categories_objects(element.categories)
                stores = StoreManager().get_stores_objects(element.stores)

                product.categories.add(*categories)
                product.stores.add(*stores)


    def get_all_product_by_category(self):
        pass

    def get_all_product_by_nutriscore_inf(self, nutriscore):
        product_model = apps.get_model('core', 'Product')

        product_list = product_model.product_objects.filter(
            nutriscore_grade__lt=nutriscore).order_by('nutriscore_grade')

        return product_list

    def get_product_by_name(self, product_name):
        product_model = apps.get_model('core', 'Product')

        product = product_model.product_objects.get(product_name=product_name)

        return product

    def get_product_contains_name(self, product_name):
        product_model = apps.get_model('core', 'Product')

        products = product_model.product_objects.filter(product_name__icontains=product_name)

        if products.count() > 1:
            product = products[randint(0, len(products) - 1)]

        elif products.count() > 1:
            product = products[0]
        
        else:
            product = []

        return product


    def get_product_by_barcode(self, barcode):
        product_model = apps.get_model('core', 'Product')

        product = product_model.product_objects.get(barcode=barcode)

        return product
    

