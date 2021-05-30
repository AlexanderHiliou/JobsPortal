from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from core.models import Userprofile

USER_MODEL = get_user_model()


class SignupTestCase(TestCase):
    """Test of the signup page"""

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.url = '/accounts/signup/'
        cls.username = 'Elsa'
        cls.email = 'elsa@gmail.com'
        cls.password = '8096546qWe'
        cls.password2 = '8096546qWe'
        cls.data = {
            'username': cls.username,
            'email': cls.email,
            'password1': cls.password,
            'password2': cls.password2,
        }

    def test_get_signup(self):
        """Tests that a GET request works and renders the correct template"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_form_fields(self):
        """Tests that only specified fields are displayed in the signup form"""
        response = self.client.get(self.url)
        form = response.context_data['form']
        self.assertEqual(len(form.fields), 4)
        self.assertIn('email', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('password1', form.fields)
        self.assertIn('password2', form.fields)

    def test_signup_form_employer(self):
        """Tests that after a POST request employer will be redirected to the new_company page"""
        self.data['account_type'] = 'employer'
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('new_company'))

    def test_signup_form_jobseeker(self):
        """Tests that after a POST request jobseeker will be redirected to the frontpage"""
        self.data['account_type'] = 'jobseeker'
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
