from django.test import TestCase
from django.urls import reverse


from core.models.product import Product


class SubstituteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_product = 12

        for product_id in range(number_of_product):
            Product.product_objects.create_product(
                barcode=product_id,
                product_name=f"product_name_{product_id}",
                nutriscore_grade="A",
                product_description="Product description",
                off_url="www.off.com",
                image_url="www.image_url.com")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/substitute/?product=product_name_1')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            "%s?product=product_name_1" % reverse('substitute'))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            "%s?product=product_name_1" % reverse('substitute'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitutes/substitute.html')

    def test_pagination(self):
        response = self.client.get(
            "%s?product=product_name_1" % reverse('substitute'))

        self.assertEqual(response.status_code, 200)
        self.assertEquals(
            response.context['substitute_pages'].number,
            response.context['substitute_pages'].paginator.page(1).number)
