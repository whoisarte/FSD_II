from django.test import SimpleTestCase
from django.urls import reverse

class SimpleTestCase(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_about_page_status_code(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_content_page_status_code(self):
        response = self.client.get(reverse("content"))
        self.assertEqual(response.status_code, 200)

# Create your tests here.
