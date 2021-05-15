from django.db import models
from django.contrib.auth.models import User


class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username + ' is employer' if self.is_employer else self.user.username + ' is jobseeker'}"
