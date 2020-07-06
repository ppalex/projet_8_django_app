from django.test import TestCase
from core.models.product import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(barcode=123,
                                product_name="product_name",
                                nutriscore_grade="A",
                                product_description="Product description",
                                off_url="www.off.com")
        

    def test_product_instance(self):
        """Animals that can speak are correctly identified"""
        product = Product.objects.get(barcode=123)
        
        self.assertEqual(product.barcode, 123)
        self.assertEqual(product.product_name, "product_name")
        self.assertEqual(product.product_description, "Product description")
        self.assertEqual(product.off_url, "www.off.com")


    def test_str(self):
        product = Product.objects.get(barcode=123)

        self.assertEqual(str(product), "product_name")

    def test_create_product(self):

        product_dic = [
                        {
                            'barcode':123,
                            'product_name':"product_name",
                            'nutriscore_grade':"A",
                            'product_description':"Product description",
                            'off_url':"www.off.com"}]
        
        product_list = Product.create_product(product_dic)

        product = product_list[0]

        self.assertEquals(True, isinstance(product, Product))
        self.assertEqual(product.barcode, 123)
        self.assertEqual(product.product_name, "product_name")
        self.assertEqual(product.product_description, "Product description")
        self.assertEqual(product.off_url, "www.off.com")