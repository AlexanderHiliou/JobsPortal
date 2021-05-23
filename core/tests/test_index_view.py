import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from core.models import Userprofile
from employer.company.models import Company
from employer.job.models import Job, Category

USER_MODEL = get_user_model()


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index_view')
        self.category = Category.objects.create(
            title='Technology',
            slug='technology',
            ordering=1,
        )
        self.user = USER_MODEL.objects.create_user(
            username='Elsa',
            email='elsa@gmail.com',
            password='8096546qWe',
        )
        self.userprofile = Userprofile.objects.create(
            user=self.user, is_employer=False
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
        self.job_1 = Job.objects.create(
            title='Junior Front-end developer',
            slug='junior-front-end-developer',
            short_description='Amazing oportunity to start ur carrier',
            category=self.category,
            company=self.company,
            location='Helsinki, Finland',
            type_of_employment='Full time',
            salary='$ 80.000 / year',
            working_hours='45/h week',
            experience='No experience',
            academic_degree='Doctor',
            created_at=datetime.datetime.now(),
            job_detail='Join us!!!',
        )
        self.job_2 = Job.objects.create(
            title='Senior Front-end developer',
            slug='senior-front-end-developer',
            short_description='Amazing oportunity to start ur carrier',
            category=self.category,
            company=self.company,
            location='Helsinki, Finland',
            type_of_employment='Full time',
            salary='$ 80.000 / year',
            working_hours='45/h week',
            experience='No experience',
            academic_degree='Doctor',
            created_at=datetime.datetime.now(),
            job_detail='Join us!!!',
        )
        self.job_3 = Job.objects.create(
            title='Midle Front-end developer',
            slug='midle-front-end-developer',
            category=self.category,
            company=self.company,
            type_of_employment='Full time',
            salary='$ 80.000 / year',
            working_hours='45/h week',
            experience='No experience',
            academic_degree='Doctor',
            created_at=datetime.datetime.now(),
            job_detail='Join us!!!',
        )
        self.job_4 = Job.objects.create(
            title='Junior Back-end developer',
            slug='junior-back-end-developer',
            category=self.category,
            company=self.company,
            location='Helsinki, Finland',
            type_of_employment='Full time',
            salary='$ 80.000 / year',
            working_hours='45/h week',
            experience='No experience',
            academic_degree='Doctor',
            created_at=datetime.datetime.now(),
            job_detail='Join us!!!',
        )
        self.job_5 = Job.objects.create(
            title='CEO',
            slug='ceo',
            short_description='Amazing oportunity to start ur carrier',
            category=self.category,
            company=self.company,
            location='Helsinki, Finland',
            type_of_employment='Full time',
            salary='$ 80.000 / year',
            working_hours='45/h week',
            experience='No experience',
            academic_degree='Doctor',
        )
        self.job_6 = Job.objects.create(
            title='Senior Back-end developer',
            slug='senior-back-end-developer',
            short_description='Amazing oportunity to start ur carrier',
            category=self.category,
            company=self.company,
            location='Helsinki, Finland',
            type_of_employment='Full time',
            salary='$ 80.000 / year',
            working_hours='45/h week',
            experience='No experience',
            academic_degree='Doctor',
        )

    def test_index_view_url(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['object_list']), 5)
        self.assertEqual([job.id for job in response.context_data['object_list']], [6, 5, 4, 3, 2])
