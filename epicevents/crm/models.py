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

    phone = models.CharField(max_length=128, default="null")
    role = models.CharField(choices=ROLE, max_length=128, default="MANAGER")



class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=25, default=" ")
    last_name = models.CharField(max_length=25, default=" ")
    email = models.CharField(max_length=100, default=" ")
    phone = models.CharField(max_length=20, default=" ")
    mobile = models.CharField(max_length=20, default=" ")
    company_name = models.CharField(max_length=250, default=" ")
    date_created = models.DateTimeField(default=datetime.datetime.now())
    date_update = models.DateTimeField(default=datetime.datetime.now())
    statuts_client = models.CharField(choices=STATUT_CLIENT, max_length=25, default="POTENTIEL")
    employee_contact = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)


class Contract(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_contact = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, default=1)
    date_created = models.DateTimeField(default=datetime.datetime.now())
    date_update = models.DateTimeField(default=datetime.datetime.now())
    status = models.BooleanField(default=False)
    amount = models.FloatField(default=10.2)
    payment_due = models.DateTimeField(default=datetime.datetime.now())


class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, default=1)
    date_created = models.DateTimeField(default=datetime.datetime.now())
    date_update = models.DateTimeField(default=datetime.datetime.now())
    employee_contact = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="sales_contact", default=1
    )
    employee_event = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="event_contact", default=1
    )
    event_date = models.DateTimeField(default=datetime.datetime.now())
    notes = models.TextField(max_length=8192, blank=True)
    attendees = models.IntegerField(default=200)
