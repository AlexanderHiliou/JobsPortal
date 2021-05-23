from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model

from core.models import Userprofile

USER_MODEL = get_user_model()


class LoginTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.url = '/accounts/login/'
        cls.username = 'Elsa'
        cls.email = 'elsa@gmail.com'
        cls.password = '8096546qWe'
        cls.user = USER_MODEL.objects.create_user(
            username=cls.username,
            email=cls.email,
            password=cls.password,
        )
        cls.userprofile = Userprofile.objects.create(user=cls.user, is_employer=False)

    def test_login_url(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_login_success_url(self):
        response = self.client.post(self.url, {"login": self.email, "password": self.password})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
