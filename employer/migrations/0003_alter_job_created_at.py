# Generated by Django 3.2.2 on 2021-05-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_alter_company_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания объявления'),
        ),
    ]
