from django.contrib.auth import get_user_model
from django.test import TestCase

from core.models import Userprofile
from employer.company.models import Company

USER_MODEL = get_user_model()


class CompanyModelTestCase(TestCase):
    """Tests of Company model"""
    def setUp(self):
        self.user = USER_MODEL.objects.create_user(
            username='Elsa',
            email='elsa@gmail.com',
            password='8096546qWe',
        )
        self.userprofile = Userprofile.objects.create(
            user=self.user, is_employer=True
        )
        self.company = Company.objects.create(
            name='Google',
            slug='google',
            employer=self.userprofile,
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

    def test_create_company(self):
        """Tests that company has been created"""
        self.assertEqual(self.company.name, 'Google')
        self.assertEqual(Company.objects.all().count(), 1)

    def test_company_str(self):
        """Tests the __str__ of the Company model"""
        self.assertEqual(str(self.company), 'Google')


