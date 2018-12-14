from django.test import TestCase
# creating first test set
from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code, 200)
    def test_about_page_status_code(self):
        responce = self.client.get('/about/')
        self.assertEqual(responce.status_code, 200)


