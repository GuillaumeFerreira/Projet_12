from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):

    phone = models.CharField(max_length=128, blank=True)
