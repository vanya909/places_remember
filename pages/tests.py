from django.test import TestCase
from django.urls import reverse_lazy


class HomePageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_reverse_lazy_status_code(self):
        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse_lazy('home'))
        self.assertTemplateUsed(response, 'pages/home.html')
