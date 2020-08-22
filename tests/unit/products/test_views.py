from django.test import TestCase
from django.urls import reverse

from core.models.product import Product


class ProductDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_product = 1

        Product.product_objects.create_product(barcode=number_of_product,
                                               product_name=f"product_name_{number_of_product}",
                                               nutriscore_grade="A",
                                               product_description="Product description",
                                               off_url="www.off.com",
                                               image_url="www.image_url.com")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/product/1/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('product', kwargs={'barcode': 1}))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('product', kwargs={'barcode': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
