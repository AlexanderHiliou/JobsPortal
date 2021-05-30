from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from core.models import Userprofile
from employer.company.models import Company

USER_MODEL = get_user_model()


class CompanyCreateViewTestCase(TestCase):
    """Tests of Company Create View"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('new_company')
        self.user1 = USER_MODEL.objects.create_user(
            username='Elsa',
            email='elsa@gmail.com',
            password='8096546qWe',
        )
        self.user2 = USER_MODEL.objects.create_user(
            username='Gigi',
            email='gigi@gmail.com',
            password='8096546qWe',
        )
        self.user3 = USER_MODEL.objects.create_user(
            username='Amanda',
            email='amanda@gmail.com',
            password='8096546qWe',
        )
        self.userprofile_employer = Userprofile.objects.create(
            user=self.user1, is_employer=True
        )
        self.userprofile_jobseeker = Userprofile.objects.create(
            user=self.user2, is_employer=False
        )
        self.userprofile_employer_with_company = Userprofile.objects.create(
            user=self.user3, is_employer=True
        )
        self.company = Company.objects.create(
            name='Google',
            slug='google',
            employer=self.userprofile_employer_with_company,
            field_of_activity='Internet',
            short_description='We are the largest tech company in the world',
            location='Menlo Park, CA',
            created_at='1998',
            amount_of_workers='10 - 99',
            phone='+38076321238',
            website='https://www.google.com/',
            email='support.google@gmail.com',
            company_detail='Join Us now!',
        )
        self.data = {
            'name': 'facebook',
            'field_of_activity': 'Social media',
            'short_description': 'We are the largest tech company in the world',
            'location': 'Menlo Park, CA',
            'created_at': '1998',
            'amount_of_workers': '10 - 99',
            'phone': '+38076321238',
            'website': 'https://www.google.com/',
            'email': 'support.google@gmail.com',
            'company_detail': 'Join Us now!',
        }
        self.data1 = {
            'name': 'facebook',
            'field_of_activity': 'Social media',
            'short_description': 'We are the largest tech company in the world',
            'location': 'Menlo Park, CA',
            'created_at': '1998',
            'amount_of_workers': '10 - 99',
            'phone': '+38076321238',
            'website': 'https://www.google.com/',
            'email': 'support.google@gmail.com',
            'company_detail': 'Join Us now!',
        }

    def test_only_employers_allowed(self):
        """Tests that a GET request works only for employers and renders the correct template"""
        self.client.force_login(self.user1)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'company/company_add.html')

    def test_jobseeker_acsess_denied(self):
        """Tests that a GET request doesn't works for jobseekers"""
        self.client.force_login(self.user2)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_employers_with_company_acsess_denied(self):
        """Tests that a GET request doesn't works for employers who already has a company"""
        self.client.force_login(self.user3)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_success_url(self):
        """Tests that user has been redirected to the frontpage"""
        self.client.force_login(self.user1)
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_slug_generation(self):
        """Tests a slug is automatically created"""
        self.client.force_login(self.user1)
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(Company.objects.get(name=self.data['name']).slug, self.data['name'])

    # def test_slugs_are_unique(self):
    #     self.client.force_login(self.user1)
    #     response = self.client.post(self.url, self.data)
    #     response1 = self.client.post(self.url, self.data1)
    #     self.assertEqual(Company.objects.get(name=self.data['name']).slug, self.data['name'])
    #     self.assertEqual(Company.objects.get(name=self.data1['name']).slug, f'{self.data1["name"]}-1')

    def test_user_added(self):
        """Tests a user is automatically added"""
        self.client.force_login(self.user1)
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(Company.objects.get(name=self.data['name']).employer, self.userprofile_employer)

