from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

ROLE = [
    ('MANAGER', 'MANAGER'),
    ('COMMERCIAL', 'COMMERCIAL'),
    ('SUPPORT', 'SUPPORT'),
]

STATUT_CLIENT =  [
    ('POTENTIEL', 'POTENTIEL'),
    ('EXISTANT', 'EXISTANT'),
]
class Employee(AbstractUser):

    phone = models.CharField(max_length=128, blank=True)
    role = models.CharField(choices=ROLE, max_length=128, default="MANAGER")



class Client(models.Model):

    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    statuts_client = models.CharField(choices=STATUT_CLIENT, max_length=25, default="POTENTIEL")
    employee_contact = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, blank=True, null=True)


class Contract(models.Model):

    employee_contact = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contract')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()


class Event(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='event')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    employee_contact = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="sales_contact", default=1
    )
    employee_event = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="event_contact", default=1
    )
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=8192, blank=True)
    attendees = models.IntegerField()
