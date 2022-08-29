from rest_framework.serializers import ModelSerializer
from . import models


class ClientsSerializer(ModelSerializer):

    class Meta:
        model = models.Client
        fields = '__all__'


class ContractSerializer(ModelSerializer):

    class Meta:
        model = models.Contract
        fields = '__all__'


class EventSerializer(ModelSerializer):

    class Meta:
        model = models.Event
        fields = '__all__'