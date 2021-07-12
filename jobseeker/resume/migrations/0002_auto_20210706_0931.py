# Generated by Django 3.2.2 on 2021-07-06 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='school_logo',
            field=models.ImageField(blank=True, default='Default/logo-default.png', null=True, upload_to='Rest_images/', verbose_name='Лого школы'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='school_logo',
            field=models.ImageField(blank=True, default='Default/logo-default.png', null=True, upload_to='Rest_images/', verbose_name='Лого компании'),
        ),
        migrations.AlterField(
            model_name='education',
            name='date_from',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Дата поступления'),
        ),
        migrations.AlterField(
            model_name='education',
            name='date_to',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume', verbose_name='Резюме'),
        ),
        migrations.AlterField(
            model_name='education',
            name='school',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Учебное заведение'),
        ),
        migrations.AlterField(
            model_name='education',
            name='short_description',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='jobseeker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='core.userprofile', verbose_name='Cоискатель работы'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.CharField(blank=True, choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('50', '50'), ('60', '60'), ('70', '70'), ('80', '80'), ('90', '90'), ('100', '100')], default=10, max_length=75, null=True, verbose_name='Уровень владения технологией'),
        ),
    ]