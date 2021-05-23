from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from core.models import Userprofile

USER_MODEL = get_user_model()


class SignupTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.url = '/accounts/signup/'
        cls.username = 'Elsa'
        cls.email = 'elsa@gmail.com'
        cls.password = '8096546qWe'
        cls.password2 = '8096546qWe'

    def test_signup_url(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_form_fields(self):
        response = self.client.get(self.url)
        form = response.context_data['form']
        self.assertEqual(len(form.fields), 4)
        self.assertIn('email', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('password1', form.fields)
        self.assertIn('password2', form.fields)

    def test_signup_form_employer(self):
        response = self.client.post(self.url, data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password2,
            'account_type': 'employer',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('new_company'))
        self.assertEqual(USER_MODEL.objects.all().count(), 1)
        self.assertEqual(Userprofile.objects.filter(is_employer=True).count(), 1)

    def test_signup_form_jobseeker(self):
        response = self.client.post(self.url, data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password2,
            'account_type': 'jobseeker',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertEqual(USER_MODEL.objects.all().count(), 1)
        self.assertEqual(Userprofile.objects.filter(is_employer=False).count(), 1)
