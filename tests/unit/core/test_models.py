from unittest import mock

from django.conf import settings
from django.test import TestCase

from core.models.payload import Payload
from core.models.product import (Product, ProductCleaner, ProductDownloader)
from core.models.store import Store
from core.models.user import User

# Test Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.product_objects.create_product(
            barcode=123,
            product_name="product_name",
            nutriscore_grade="A",
            product_description="Product description",
            off_url="www.off.com",
            image_url="www.image_url.com")

    def test_product_instance(self):

        product = Product.product_objects.get(barcode=123)

        self.assertEqual(product.barcode, 123)
        self.assertEqual(product.product_name, "product_name")
        self.assertEqual(product.product_description, "Product description")
        self.assertEqual(product.off_url, "www.off.com")
        self.assertEqual(product.image_url, "www.image_url.com")

    def test_str(self):
        product = Product.product_objects.get(barcode=123)

        self.assertEqual(str(product), "product_name")


class ProductDownloaderTestCase(TestCase):

    @mock.patch('core.models.product.requests.get')
    def test_send_request(self, mock_get):

        results = {
            "skip": 0,
            "count": 1663,
            "page_size": "20",
            "page": 1,
            "products": [{
                "barcode": 123,
                "product_name": "Dolce pizza",
                "categories": "pizza,pizza fromage",
                "nutriscore_grade": "A",
                "stores_tags": ["carrefour-city", "franprix"],
                "ingredients_text_debug":  "Description of the product",
                "url": "www.url.com",
            }]
        }

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
            url=settings.API_OFF,
            headers={},
            payload=payload.get_payload_formatted())

        product_downloader.send_request()

        self.assertEqual(product_downloader.data_json, results)
        self.assertEqual(
            product_downloader.get_products_from_json(), results['products'])


class ProductCleanerTestCase(TestCase):

    def test_create(self):
        product = {"id": 123,
                   "product_name": "Dolce pizza",
                   "categories": "pizza, cheese pizza",
                   "nutriscore_grade": "A",
                   "stores": ["carrefour", "franprix"],
                   "ingredients_text_debug":  "Description of the product",
                   "url": "www.url.com"}

        product_cleaner = ProductCleaner()
        product_cleaner = product_cleaner.create(product, "pizza")

        self.assertEquals(True, isinstance(product_cleaner, ProductCleaner))
        self.assertEquals(product_cleaner.barcode, 123)
        self.assertEquals(product_cleaner.product_name, "Dolce pizza")
        self.assertEquals(product_cleaner.categories,
                          ["pizza", " cheese pizza"])

    def test_format_categories(self):
        pass

    def test_split_categories(self):
        pass

    def test_split_string(self):
        pass


# Test Payload


class PayloadTestCase(TestCase):

    def test_get_payload_formatted(self):
        payload = Payload(
            action=settings.PAYLOAD['action'],
            tag_0=settings.PAYLOAD['tag_0'],
            tag_contains_0=settings.PAYLOAD['tag_contains_0'],
            tagtype_0=settings.PAYLOAD['tagtype_0'],
            page_size=1,
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


# Test Category

# Test Store


class StoreTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Store.store_objects.create(store_name="store_name")

    def test_store_name_label(self):
        store = Store.store_objects.get(store_id='1')
        store_name_label = store._meta.get_field('store_name').verbose_name

        self.assertEquals(store_name_label, 'store name')


# Test User

class UserTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="APP",
                            password="12345",
                            email="app@gmail.com")

    def test_username_label(self):
        user = User.objects.get(user_id='1')
        username_label = user._meta.get_field('username').verbose_name

        self.assertEquals(username_label, 'username')

    def test_password_label(self):
        user = User.objects.get(user_id='1')
        password_label = user._meta.get_field('password').verbose_name

        self.assertEquals(password_label, 'password')

    def test_email_label(self):
        user = User.objects.get(user_id='1')
        email_label = user._meta.get_field('email').verbose_name

        self.assertEquals(email_label, 'email')
