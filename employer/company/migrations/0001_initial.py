# Generated by Django 3.2.2 on 2021-05-18 11:30

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import employer.company.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Название компании')),
                ('field_of_activity', models.CharField(max_length=75, verbose_name='Сфера деятельности')),
                ('short_description', models.TextField(max_length=400, verbose_name='Краткое описание')),
                ('location', models.CharField(max_length=75, verbose_name='Локация')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=employer.company.models.Company.load_photo, verbose_name='Лого')),
                ('created_at', models.CharField(max_length=4, verbose_name='Год создания')),
                ('amount_of_workers', models.CharField(choices=[('0 - 9', '0 - 9'), ('10 - 99', '10 - 99'), ('100 - 999', '100 - 999'), ('1,000 - 9,999', '1,000 - 9,999'), ('10,000 - 99,999', '10,000 - 99,999'), ('100,000 - 999,999', '100,000 - 999,999')], default='10 - 99', max_length=20, verbose_name='Количество работников')),
                ('phone', models.CharField(max_length=75, verbose_name='Номер телефона')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Адрес вебсайта')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('slug', models.SlugField(max_length=75, unique=True)),
                ('facebook_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на фейсбук компании')),
                ('google_plus_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на гугл+ компании')),
                ('dribbble_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на дрибл компании')),
                ('pinterest_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на пинтерест компании')),
                ('twitter_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на твиттер компании')),
                ('linkedin_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на линкедин компании')),
                ('instagram_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на инстаграм компании')),
                ('youtube_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на ютуб компании')),
                ('company_detail', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Полное описание')),
                ('employer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='core.userprofile', verbose_name='Работодатель')),
            ],
        ),
    ]