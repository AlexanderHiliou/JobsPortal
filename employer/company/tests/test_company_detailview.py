from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from core.models import Userprofile
from employer.company.models import Company

USER_MODEL = get_user_model()


class CompanyDetaiViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = USER_MODEL.objects.create_user(
            username='Elsa',
            email='elsa@gmail.com',
            password='8096546qWe',
        )
        self.userprofile_employer = Userprofile.objects.create(
            user=self.user1, is_employer=True
        )
        self.company = Company.objects.create(
            name='Google',
            slug='google',
            employer=self.userprofile_employer,
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
        self.url = reverse('company_detail', args=(self.company.slug,))

    def test_get_company_detail(self):
        """Tests that a GET request works as expected"""
        self.client.force_login(self.user1)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'company/company_detail.html')
