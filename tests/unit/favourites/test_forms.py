from django.test import TestCase
from core.models.user import User
from core.models.product import Product

from django.urls import reverse


class DeleteFavouriteFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK')

        number_of_product = 1

        for product_id in range(number_of_product):
            product = Product.product_objects.create_product(
                barcode=product_id,
                product_name=f"product_name_{product_id}",
                nutriscore_grade="A",
                product_description="Product description",
                off_url="www.off.com",
                image_url="www.image_url.com")
            user1.product_set.add(product)

    def test_delete_submit_button(self):
        self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')

        response = self.client.post(self.client.get(
            reverse('favourite')),
            {'action': 'Supprimer', 'substitute_barcode': 0})

        response = self.client.get(reverse('favourite'))
        self.assertEqual(response.status_code, 200)
