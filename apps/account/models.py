from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    is_seeker = models.BooleanField(default=False)
    bio = models.CharField(max_length=255, default='', blank=True)
    address_line_1 = models.CharField(max_length=255, default='', blank=True)
    address_line_2 = models.CharField(max_length=255, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    province = models.CharField(max_length=100, default='', blank=True)
    postal_code = models.CharField(max_length=20, default='', blank=True)
