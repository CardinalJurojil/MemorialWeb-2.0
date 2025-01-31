from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)