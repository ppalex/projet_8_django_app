from django.db import models

from django.apps import apps

from django.db import IntegrityError
import logging


class StoreManager(models.Manager):

    def create_store(self, store_name):
        """This method create a store object.

        Returns:
            [Object]: Store object.
        """

        store_model = apps.get_model('core', 'Store')

        try:
            store = store_model.store_objects.create(store_name=store_name)

            return store

        except IntegrityError:
            logging.info("Integrity violation")
            return None

    def get_stores_objects(self, store_list):
        """This method get the categories from the db, based on
        the category name from a list.

        Returns:
            [List]: Contains Stores from the db.
        """
        stores = []
        store_model = apps.get_model('core', 'Store')

        for store in store_list:
            try:
                selected_store = store_model.store_objects.get(
                    store_name=store)
                stores.append(selected_store)

            except store_model.DoesNotExist:
                stores.append(
                    store_model.store_objects.create(store_name=store))

        return stores
