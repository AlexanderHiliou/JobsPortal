from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model

from core.models import Userprofile

USER_MODEL = get_user_model()


class LoginTestCase(TestCase):
    """Test of the login page"""
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

    def test_get_login(self):
        """Tests that a GET request works and renders the correct template"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_form_fields(self):
        """Tests that only login and password fields are displayed in the user form"""
        response = self.client.get(self.url)
        form = response.context_data['form']
        self.assertEqual(len(form.fields), 3)
        self.assertIn('login', form.fields)
        self.assertIn('password', form.fields)

    def test_login_success_url(self):
        """Tests that after a POST request user will be redirected to the frontpage"""
        response = self.client.post(self.url, {"login": self.email, "password": self.password})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
