from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from core.models import Userprofile
from employer.company.models import Company
from employer.job.models import Category, Job

USER_MODEL = get_user_model()


class JobCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('job_add')
        self.user1 = USER_MODEL.objects.create(
            username='Elsa',
            email='elsa@gmail.com',
            password='8096546qWe',
        )
        self.user2 = USER_MODEL.objects.create_user(
            username='Gigi',
            email='gigi@gmail.com',
            password='8096546qWe',
        )
        self.userprofile_employer = Userprofile.objects.create(
            user=self.user1, is_employer=True
        )
        self.userprofile_jobseeker = Userprofile.objects.create(
            user=self.user2, is_employer=False
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
        self.category = Category.objects.create(
            title='Technology',
            slug='technology',
            ordering='1',
        )
        self.data = {
            'title': 'Senior back-end developer',
            'short_description': 'Senior back-end developer',
            'category': self.category.id,
            'application_url': 'https://www.facebook.com/',
            'location': 'Minsk, Belarus',
            'type_of_employment': 'Full time',
            'salary': '80.000$ / year',
            'working_hours': '45 / week',
            'experience': '7 years',
            'academic_degree': 'Bachelor',
            'job_detail': 'Senior back-end developer',
        }

    def test_get_job_create(self):
        """Tests that a GET request works as expected and only for employers"""
        self.client.force_login(self.user1)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'job/job_add.html')

    def test_jobseeker_access_denied(self):
        """Tests that a GET request denied for jobseekers"""
        self.client.force_login(self.user2)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_employer_able_to_create(self):
        """Tests that a POST request createing an instance"""
        self.client.force_login(self.user1)
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(Job.objects.get(title=self.data['title']).title, self.data['title'])

    def test_slug_auto_created(self):
        self.client.force_login(self.user1)
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(Job.objects.get(title=self.data['title']).slug, 'senior-back-end-developer')

    def test_success_url(self):
        """Tests that a POST request redirect to job detail page"""
        self.client.force_login(self.user1)
        response = self.client.post(self.url, data=self.data)
        job = Job.objects.get(title=self.data['title'])
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             reverse('job_detail', kwargs={'company_slug': job.company.slug, 'slug': job.slug}))
