from django.db import models

from django.apps import apps

from django.db import IntegrityError
import logging


class CategoryManager(models.Manager):

    def create_category(self, category_name):
        """This method create a category object.

        Returns:
            [Object]: Category object.
        """

        category_model = apps.get_model('core', 'Category')

        try:
            category = category_model.category_objects.create(
                category_name=category_name)

            return category

        except IntegrityError:
            logging.error("Integrity violation")
            return None

    def get_categories_objects(self, category_list):
        """This method get the categories from the db, based on
        the category name from a list.

        Returns:
            [List]: Contains Categories from the db.
        """
        categories = []
        category_model = apps.get_model('core', 'Category')

        for category in category_list:
            try:
                selected_category = category_model.category_objects.get(
                    category_name=category)
                categories.append(selected_category)

            except category_model.DoesNotExist:
                categories.append(
                    category_model.category_objects.create(
                        category_name=category))

        return categories
