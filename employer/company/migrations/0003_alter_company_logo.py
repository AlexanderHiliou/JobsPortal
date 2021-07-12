# Generated by Django 3.2.2 on 2021-05-31 23:32

from django.db import migrations, models
import employer.company.models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20210518_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='Default/logo-default.png', null=True, upload_to=employer.company.models.Company.load_photo, verbose_name='Лого'),
        ),
    ]
