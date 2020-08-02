from django.test import TestCase
from django.urls import reverse

from core.models.product import Product
from core.models.user import User

class FavouriteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')


        number_of_product = 12

        for product_id in range(number_of_product):
            product =  Product.product_objects.create_product(barcode=product_id,
                                                    product_name=f"product_name_{product_id}",
                                                    nutriscore_grade="A",
                                                    product_description="Product description",
                                                    off_url="www.off.com",
                                                    image_url="www.image_url.com")
            user1.product_set.add(product)


    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('favourite'))
        self.assertRedirects(response, '/login/?next=/favourites/')


    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('favourite'))
        
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'favourites/favourites.html')

    def test_pagination(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('favourite'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['favourites']) == 6)
        
    def test_lists_all_favourites(self):

        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('favourite'))

        # Get second page and confirm it has (exactly) remaining 6 items
        response = self.client.get(reverse('favourite')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['favourites']) == 6)






    