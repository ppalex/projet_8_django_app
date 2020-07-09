import requests

from django.db import models

from .category import Category
from .store import Store

from core.managers.product_manager import ProductManager

class Product(models.Model):
    
    barcode = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    nutriscore_grade = models.CharField(max_length=4)
    product_description = models.TextField()
    off_url = models.CharField(max_length=255)
    
    categories = models.ManyToManyField(Category)
    stores = models.ManyToManyField(Store)
    substitutes = models.ManyToManyField("self")

    product_objects = ProductManager()    

    def __str__(self):
        return self.product_name


class ProductDownloader:
    def __init__(self, url, headers, payload):
        """Constructor of the class ProductDownloader.

        Arguments:
            url {String} -- Contains the url for api request.
            headers {String} -- Contains the header for api request.
            payload {Object} -- Contains Payload object for api request.
        """
        self.url = url
        self.headers = headers
        self.payload = payload

    def send_request(self):
        """This method send a request on the url API.

        Returns:
            [Response] -- The response contains the data from api request
                            in Json format.
        """
        
        response = requests.get(self.url, headers=self.headers, params=self.payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None


class ProductCleaner:
    def __init__(self, **product_attributes):
        for attr_name, attr_value in product_attributes.items():
            setattr(self, attr_name, attr_value)


    def __str__(self):
        """This method return an object Product in String format
        """
        string = ""
        attr = vars(self)
        for k, v in attr.items():
            string += f"{k} : {v} \n"
        return string

    @classmethod
    def create(cls, product, category):
        """This method creates a list of Product from a list of dictionnaries.
            The method get from the dictionnary the information needed.
            Information not needed are not stored in Products objects.
        Arguments:
            products {List} -- Contains the dictionnaries.
            category {String} -- The category represents the category from
                                which the element of the list are recovered.

        Returns:
            [List] -- List of Product.
        """
        
        product_cleaner = cls(**{
                'barcode': product.get('id', None),
                'product_name': product.get('product_name', None),
                'category': category,
                'nutriscore_grade': product.get('nutriscore_grade', None),
                'categories': product.get('categories', "").split(','),
                'stores': product.get('stores_tags', []),
                'description': product.get('ingredients_text_debug', None),
                'off_url': product.get('url', None)})
        
        return product_cleaner

    
    def format_categories(self):
        """[summary]

        Arguments:
            product_list {[type]} -- [description]
        """
        for product in product_list:
            categories = []
            for category in product.categories:
                categories.append(category.lstrip().rstrip())
            setattr(product, 'categories', categories)

    def split_categories(self):
        """This method splits categories from a list of Product.

        Arguments:
            product_list {List} -- This list contains Products;
        """
        for product in product_list:
            self.split_string(product)

    @staticmethod
    def split_string(product):
        """This method split a string into list.

        Arguments:
            product {Object} -- Represent a Product.
        """
        setattr(product, 'categories', product.categories.split(','))


class ProductInventory:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)