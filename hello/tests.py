# Run tests with "manage.py test".

from django import http
from django.test import TestCase

from . import views


class HomeViewTest(TestCase):
    def test_home(self):
        requst = http.HttpRequest()
        home = view.Home()
        response = get(request)
        self.assertEqual(200, response.status_code)
        self.assertIn('Hello World!', response.content)
