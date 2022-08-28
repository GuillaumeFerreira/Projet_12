from rest_framework.serializers import ModelSerializer
from . import models

class ClientsSerializer(ModelSerializer):
    class Meta:
        model = models.Client
        fields = ["id", "first_name", "last_name", "email"]

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ["id","team", "first_name", "last_name", "email"]

class TeamSerializer(ModelSerializer):
    class Meta:
        model = models.Team
        fields = ["id","type_team"]

class ContractSerializer(ModelSerializer):
    class Meta:
        model = models.Contract
        fields = ["id","date_created", "date_update","status","amount","payment_due"]

class EventSerializer(ModelSerializer):
    class Meta:
        model = models.Event
        fields = ["id","date_created", "date_update","notes","attendees"]