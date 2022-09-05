from django.db import models
from management.models import Employee


STATUT_CLIENT = [
    ("POTENTIEL", "POTENTIEL"),
    ("EXISTANT", "EXISTANT"),
]

STATUS_EVENT = [
    ("EN PREPARATION", "EN PREPARATION"),
    ("EN COURS", "EN COURS"),
    ("TERMINE", "TERMINE"),
]


class Client(models.Model):

    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    statuts_client = models.CharField(
        choices=STATUT_CLIENT, max_length=25, default="POTENTIEL"
    )
    employee_contact = models.ForeignKey(
        Employee, on_delete=models.DO_NOTHING, blank=True, null=True
    )


class Contract(models.Model):

    contract_name = models.CharField(max_length=128, blank=False, null=False)
    employee_contact = models.ForeignKey(
        Employee, on_delete=models.DO_NOTHING, default=1
    )
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="contract"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    signed = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()

class Event_status(models.Model):
    status = models.CharField(choices=STATUS_EVENT, max_length=128, default="EN PREPARATION")

class Event(models.Model):

    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, related_name="event"
    )
    event_status = models.ForeignKey(
        Event_status, on_delete=models.CASCADE, related_name="status_event"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    employee_event = models.ForeignKey(
        Employee, on_delete=models.DO_NOTHING, related_name="event_contact", default=1
    )
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=8192, blank=True)
    attendees = models.IntegerField()