from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from core.models.user import User
from core.models.product import Product
from core.models.category import Category
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.urls import reverse

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

class ChromeFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Chrome web browser in headless mode."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.close()        

    def setUp(self):     

        user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')

    def test_user_can_connect(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_id('id_login').click()

        self.driver.find_element_by_id('id_username').send_keys(
            "testuser1"
        )
        self.driver.find_element_by_id('id_password').send_keys(
            "1X<ISRUkw+tuK"
        )       

        self.driver.find_element_by_id('id_button_login').send_keys(Keys.RETURN)
        
        message = self.driver.find_element_by_id('msg')

        self.assertEqual(
            message.text,
            "Vous êtes connectés testuser1")

