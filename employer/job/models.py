from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.humanize.templatetags import humanize

from employer.company.models import Company


class Category(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, unique=True)
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['ordering']


class Job(models.Model):
    employment_types = [
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
        ('Remote', 'Remote'),

    ]

    degree = [
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('Postdoc', 'Postdoc'),
        ('Doctor', 'Doctor'),
    ]

    title = models.CharField(max_length=75, verbose_name='Название работы')
    short_description = models.TextField(max_length=400, verbose_name='Краткое описание')
    category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='jobs', on_delete=models.CASCADE)
    application_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на вакансию')
    location = models.CharField(max_length=75, verbose_name='Локация')
    type_of_employment = models.CharField(max_length=10, choices=employment_types, default='Full time',
                                          verbose_name='Вид трудоустройства')
    salary = models.CharField(max_length=75, verbose_name='Зарплата')
    working_hours = models.CharField(max_length=75, verbose_name='Часы работы')
    experience = models.CharField(max_length=75, verbose_name='Опыт работы')
    academic_degree = models.CharField(max_length=75, choices=degree, default='', null=True, blank=True,
                                       verbose_name='Ученая степень')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания объявления')
    slug = models.SlugField(max_length=75, unique=True)
    job_detail = RichTextField(blank=True, null=True, verbose_name='Полное описание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'company_slug': self.company.slug, 'slug': self.slug})

    def get_date(self):
        return humanize.naturaltime(self.created_at)
