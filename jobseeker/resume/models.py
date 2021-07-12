from ckeditor.fields import RichTextField
from django.db import models

from taggit.managers import TaggableManager

from core.models import Userprofile


class Resume(models.Model):
    def load_photo(self, file_name):
        file_type = file_name.split(".")[-1]
        file_name = ".".join(['Profile_pictures/{}_{}', file_type])
        return file_name.format(
            self.jobseeker,
            self.full_name
        )

    def load_background(self, file_name):
        file_type = file_name.split(".")[-1]
        file_name = ".".join(['Profile_pictures/{}_{}_background', file_type])
        return file_name.format(
            self.jobseeker,
            self.full_name
        )

    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    jobseeker = models.ForeignKey(Userprofile, related_name='resumes', null=True, blank=True,
                                  on_delete=models.CASCADE, verbose_name='Cоискатель работы')
    profile_picture = models.ImageField(upload_to=load_photo, default='Default/avatar.jpg', null=True, blank=True,
                                        verbose_name='Фото')
    background_picture = models.ImageField(upload_to=load_photo, null=True, blank=True,
                                           verbose_name='Задний фон')
    headline = models.CharField(max_length=75, verbose_name='Заголовок')
    short_description = models.TextField(max_length=400, verbose_name='Краткое описание')
    location = models.CharField(max_length=75, verbose_name='Локация')
    salary = models.CharField(max_length=75, verbose_name='Зарплата')
    slug = models.SlugField(max_length=75, unique=True)
    tags = TaggableManager()
    phone = models.CharField(max_length=75, verbose_name='Номер телефона')
    website = models.URLField(null=True, blank=True, verbose_name='Адрес вебсайта')
    age = models.SmallIntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name='Почта')
    facebook_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на фейсбук компании')
    google_plus_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на гугл+ компании')
    dribbble_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на дрибл компании')
    pinterest_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на пинтерест компании')
    twitter_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на твиттер компании')
    github_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на гитхаб компании')
    instagram_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на инстаграм компании')
    youtube_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на ютуб компании')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания резюме')

    def __str__(self):
        return f'Resume of {self.full_name} - {self.headline}'


class Education(models.Model):
    degree = [
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('Postdoc', 'Postdoc'),
        ('Doctor', 'Doctor'),
    ]

    academic_degree = models.CharField(max_length=75,  choices=degree, default='Bachelor', null=True, blank=True,
                                       verbose_name='Ученая степень')
    school_logo = models.ImageField(upload_to='Rest_images/', default='Default/logo-default.png', null=True, blank=True,
                                        verbose_name='Лого школы')
    major = models.CharField(max_length=100, null=True, blank=True, verbose_name='Специальность')
    school = models.CharField(max_length=100, null=True, blank=True, verbose_name='Учебное заведение')
    date_from = models.SmallIntegerField(null=True, blank=True, verbose_name='Дата поступления')
    date_to = models.SmallIntegerField(null=True, blank=True, verbose_name='Дата окончания')
    short_description = models.TextField(null=True, blank=True, max_length=200, verbose_name='Краткое описание')
    resume = models.ForeignKey(Resume, default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Резюме')

    def __str__(self):
        return self.academic_degree


class Skill(models.Model):
    per_cent = [
        ('10', '10'),
        ('20', '20'),
        ('30', '30'),
        ('40', '40'),
        ('50', '50'),
        ('60', '60'),
        ('70', '70'),
        ('80', '80'),
        ('90', '90'),
        ('100', '100'),
    ]
    name = models.CharField(max_length=100, verbose_name='Название технологии')
    proficiency = models.CharField(max_length=75, choices=per_cent, default=10, null=True, blank=True,
                                   verbose_name='Уровень владения технологией')
    resume = models.ForeignKey(Resume, default=None, on_delete=models.CASCADE, verbose_name='Резюме')

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100, verbose_name='Название компании')
    school_logo = models.ImageField(upload_to='Rest_images/', default='Default/logo-default.png', null=True, blank=True,
                                        verbose_name='Лого компании')
    position = models.CharField(max_length=100, verbose_name='Должность')
    date_from = models.DateField(verbose_name='Дата начала работы')
    date_to = models.DateField(verbose_name='Дата завершения работы')
    job_detail = RichTextField(blank=True, null=True, verbose_name='Полное описание')
    resume = models.ForeignKey(Resume, default=None, on_delete=models.CASCADE, verbose_name='Резюме')

    def __str__(self):
        return self.company_name
