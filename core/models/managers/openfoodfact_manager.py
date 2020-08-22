from django.conf import settings

from core.models.product import ProductDownloader, ProductCleaner
from core.models.payload import Payload


class OffManager:
    def __init__(self):
        """Constructor of the class OffManager.
        """
        self.data = []

    def download_product(self):
        """This method download products by category from openfoodfact api.
             The data are recovered in self.data.

        Arguments:
            category_list {List} -- List of products categories.
        """
        url = settings.API_OFF
        headers = {}

        category_list = settings.CATEGORIES

        for category in category_list:
            payload = Payload(
                action=settings.PAYLOAD['action'],
                tag_0=category,
                tag_contains_0=settings.PAYLOAD['tag_contains_0'],
                tagtype_0=settings.PAYLOAD['tagtype_0'],
                page_size=settings.PAYLOAD['page_size'],
                json=settings.PAYLOAD['json'])

            product_downloader = ProductDownloader(
                url, headers, payload.get_payload_formatted())
            product_downloader.send_request()

            products_list = product_downloader.get_products_from_json()

            product_cleaner = ProductCleaner()
            product_cleaner_list = product_cleaner.create_list_product_cleaner(
                products_list, category)

            product_cleaner.format_categories(product_cleaner_list)

            self.data += product_cleaner_list

    def get_all_categories(self):
        """This method get all categories from products recovered in self.data.

        Returns:
            [List] -- Contains all the possible categories from products.
        """
        product_list = self.data
        return [category for product in product_list
                for category in product.categories]

    def get_all_stores(self):
        """This method get all stores from products recovered in self.data.

        Returns:
            [List] -- Contains all the possible categories from products.
        """
        product_list = self.data

        return [store for product in product_list
                for store in product.stores]
