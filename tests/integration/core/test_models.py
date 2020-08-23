from unittest import mock

from django.conf import settings
from django.test import TestCase

from core.models.managers.openfoodfact_manager import OffManager
from core.models.product import ProductCleaner


class TestOffManager(TestCase):

    @mock.patch('core.models.product.requests.get')
    def test_download_product(self, mock_get):

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

        mock_get().status_code = 200
        mock_get().json.return_value = results

        settings.CATEGORIES = ['TestCat']

        off_manager = OffManager()
        off_manager.download_product()

        data = off_manager.data

        self.assertEqual(len(data), 1)
        self.assertTrue(isinstance(data[0], ProductCleaner))
