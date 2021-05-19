from django.contrib import admin

from employer.job.models import Job, Category

admin.site.register(Job)
admin.site.register(Category)
