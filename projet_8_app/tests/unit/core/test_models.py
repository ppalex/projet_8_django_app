from django.test import TestCase
from core.models.product import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(barcode=123, product_name="one_product")
        

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        product = Product.objects.get(barcode=123)
        
        self.assertEqual(product.barcode, 123)