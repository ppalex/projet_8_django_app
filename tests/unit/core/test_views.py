from django.test import TestCase
from django.urls import reverse


from core.models.product import Product

class SubstituteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_product = 12

        for product_id in range(number_of_product):
            Product.product_objects.create_product(barcode=product_id,
                                                    product_name=f"product_name_{product_id}",
                                                    nutriscore_grade="A",
                                                    product_description="Product description",
                                                    off_url="www.off.com",
                                                    image_url="www.image_url.com")

    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/substitute/?product=product_name_1')

        self.assertEqual(response.status_code, 200)