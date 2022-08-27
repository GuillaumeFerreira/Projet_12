from django.db import models


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_team = models.CharField(max_length=128)


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    employee_contact = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Contract(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_contact = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    employee_contact = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="sales_contact")
    employee_event = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="event_contact")
    event_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=8192, blank=True)
    attendees = models.IntegerField()





