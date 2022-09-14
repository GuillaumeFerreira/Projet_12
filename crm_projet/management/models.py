from django.db import models, transaction
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):

    phone = models.CharField(max_length=128, blank=True)

    def save(self, *args, **kwargs):
        user = super(Employee, self)

        if len(user.password) != 88:
            user.set_password(self.password)
        user.save()
        return user
