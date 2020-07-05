# from django.conf import settings

# class ApiManager:
#     def __init__(self):
#         """Constructor of the class ApiManager.
#         """
#         self.data = None

#     def download_product(self, category_list):
#         """This method download products by category from openfoodfact api.
#              The data are recovered in self.data.

#         Arguments:
#             category_list {List} -- List of products categories.
#         """
#         url = settings.API_OFF
#         headers = {}
#         data = []

#         for category in category_list:
#             payload = Payload(
#                 action=config.value['PAYLOAD']['action'],
#                 tag_0=category,
#                 tag_contains_0=config.value['PAYLOAD']['tag_contains_0'],
#                 tagtype_0=config.value['PAYLOAD']['tagtype_0'],
#                 page_size=config.value['PAYLOAD']['page_size'],
#                 json=config.value['PAYLOAD']['json'])

#             product_downloader = ProductDownloader(
#                 url, headers, payload.get_payload_formatted())
#             products_data = product_downloader.load_data_source()
#             product_cleaner = ProductCleaner.create(
#                 products_data, category)
#             ProductCleaner.format_categories(product_cleaner)
#             data += product_cleaner

#         self.data = data

#     def get_all_categories(self):
#         """This method get all categories from products recovered in self.data.

#         Returns:
#             [List] -- Contains all the possible categories from products.
#         """
#         product_list = self.data
#         return [category for product in product_list
#                 for category in product.categories]

#     def get_all_stores(self):
#         """This method get all stores from products recovered in self.data.

#         Returns:
#             [List] -- Contains all the possible categories from products.
#         """
#         product_list = self.data

#         return [store for product in product_list
#                 for store in product.stores]