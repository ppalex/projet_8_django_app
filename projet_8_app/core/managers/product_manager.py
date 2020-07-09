from django.db import models

class ProductManager(models.Manager):
    
    def create_product(self, barcode, product_name, nutriscore_grade, product_description, off_url):
        product = self.create(
                                barcode=barcode,
                                product_name=product_name,
                                nutriscore_grade=nutriscore_grade,
                                product_description=product_description,
                                off_url=off_url)
        return product
