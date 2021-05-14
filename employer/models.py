from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

from core.models import Userprofile


class Company(models.Model):
    amount = [
        ('0 - 9', '0 - 9'),
        ('10 - 99', '10 - 99'),
        ('100 - 999', '100 - 999'),
        ('1,000 - 9,999', '1,000 - 9,999'),
        ('10,000 - 99,999', '10,000 - 99,999'),
        ('100,000 - 999,999', '100,000 - 999,999'),

    ]

    def load_photo(self, file_name):
        file_type = file_name.split(".")[-1]
        file_name = ".".join(['{}/{}_logo', file_type])
        return file_name.format(
            self.name,
            self.name
        )

    name = models.CharField(max_length=75, verbose_name='Название компании')
    employer = models.OneToOneField(Userprofile, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Работодатель')
    field_of_activity = models.CharField(max_length=75, verbose_name='Сфера деятельности')
    short_description = models.TextField(max_length=400, verbose_name='Краткое описание')
    location = models.CharField(max_length=75, verbose_name='Локация')
    logo = models.ImageField(upload_to=load_photo, null=True, blank=True, verbose_name='Лого')
    created_at = models.CharField(max_length=4, verbose_name='Год создания')
    amount_of_workers = models.CharField(max_length=20, choices=amount, default='10 - 99',
                                         verbose_name='Количество работников')
    phone = models.CharField(max_length=75, verbose_name='Номер телефона')
    website = models.URLField(null=True, blank=True, verbose_name='Адрес вебсайта')
    email = models.EmailField(verbose_name='Почта')
    slug = models.SlugField(max_length=75, unique=True)
    facebook_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на фейсбук компании')
    google_plus_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на гугл+ компании')
    dribbble_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на дрибл компании')
    pinterest_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на пинтерест компании')
    twitter_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на твиттер компании')
    linkedin_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на линкедин компании')
    instagram_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на инстаграм компании')
    youtube_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на ютуб компании')
    company_detail = RichTextField(blank=True, null=True, verbose_name='Полное описание')

    def __str__(self):
        return self.name


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
    created_at = models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания объявления')
    slug = models.SlugField(max_length=75, unique=True)
    job_detail = RichTextField(blank=True, null=True, verbose_name='Полное описание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'slug': self.slug})
