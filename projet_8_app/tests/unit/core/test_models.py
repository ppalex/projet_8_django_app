from unittest import mock

from django.conf import settings
from django.test import TestCase

from core.models.product import Product, requests, ProductDownloader, ProductCleaner
from core.models.payload import Payload



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
        
        
class ProductDownloaderTestCase(TestCase):    
     
        @mock.patch('core.models.product.requests.get')
        def test_send_request(self, mock_get):

            results = [
                        {
                            "skip": 0,
                            "count": 1663,
                            "page_size": "20",
                            "page": 1,
                            "products": [{
                                "barcode": 123,
                                "product_name": "Dolce pizza",
                                "categories": ["pizza", "pizza fromage"],
                                "nutriscore_grade": "A",
                                "stores_tags": ["carrefour-city", "franprix"],
                                "ingredients_text_debug":  "Description of the product",
                                "url": "www.url.com",
                            }]
                        }]

            payload = Payload(
                    action=settings.PAYLOAD['action'],
                    tag_0='pizza',
                    tag_contains_0=settings.PAYLOAD['tag_contains_0'],
                    tagtype_0=settings.PAYLOAD['tagtype_0'],
                    page_size=settings.PAYLOAD['page_size'],
                    json=settings.PAYLOAD['json'])       


            
            mock_get().status_code = 200
            mock_get().json.return_value = results

            product_downloader = ProductDownloader(
                url=settings.API_OFF, headers={}, payload=payload.get_payload_formatted())

            response = product_downloader.send_request()
            
            self.assertEqual(response, results)


class ProductCleanerTestCase(TestCase):
    
    def test_create(self):
        product_list_dic = [{
                                "products": [                                  
                                    {
                                        "barcode": 123,
                                        "product_name": "Dolce pizza",
                                        "categories": ["pizza", "pizza fromage"],
                                        "nutriscore_grade": "A",
                                        "stores_tags": ["carrefour-city", "franprix"],
                                        "ingredients_text_debug":  "Description of the product",
                                        "url": "www.url.com"},
                                    {
                                        "barcode": 1234,
                                        "product_name": "Proschuitto",
                                        "categories": ["pizza"],
                                        "nutriscore_grade": "B",
                                        "stores_tags": ["carrefour-city"],
                                        "ingredients_text_debug":  "Description of the product",
                                        "url": "www.url.com"}]}]

        product_cleaner = ProductCleaner()
        product_cleaner_list = product_cleaner.create(product_list_dic, "pizza")

        product_one = product_cleaner_list[0]
        product_two = product_cleaner_list[1]

        self.assertEquals(True, isinstance(product_one, Product))
        self.assertEquals(True, isinstance(product_two, Product))


    def test_format_categories(self):
        pass

    def test_split_categories(self):
        pass

    def test_split_string(self):
        pass



class PayloadTestCase(TestCase):
    
    def test_get_payload_formatted(self):
        payload = Payload(
            action=settings.PAYLOAD['action'],
            tag_0=settings.PAYLOAD['tag_0'],
            tag_contains_0=settings.PAYLOAD['tag_contains_0'],
            tagtype_0=settings.PAYLOAD['tagtype_0'],
            page_size=settings.PAYLOAD['page_size'],
            json=settings.PAYLOAD['json'])            
        
        payload_formatted = {
                                "action": "process",
                                "tagtype_0": "categories",
                                "tag_contains_0": "contains",
                                "tag_0": "",
                                "page_size": 1,
                                "json": True
                                }
        
        result = payload.get_payload_formatted()
        
        self.assertEqual(payload_formatted, result)
            