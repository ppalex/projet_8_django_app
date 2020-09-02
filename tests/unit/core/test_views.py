from django.test import TestCase, RequestFactory
from django.urls import reverse

from core.models.product import Product

from core.views import autocomplete
from unittest import mock


class IndexViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)


class AutocompleteTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.factory = RequestFactory()

        Product.product_objects.create_product(
            barcode=1,
            product_name="product_name",
            nutriscore_grade="A",
            product_description="Product description",
            off_url="www.off.com",
            image_url="www.image_url.com")

    def test_autocomplete(self):
        data = {'term': 'p'}
        request = self.factory.get('/autocomplete', data)

        json_response = autocomplete(request)

        self.assertJSONEqual(
            str(json_response.content, encoding='utf8'),
            ['product_name']
        )
