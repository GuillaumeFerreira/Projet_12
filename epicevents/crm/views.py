from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models, serializers, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend


class ClientsViewset(ModelViewSet):

    permission_classes = (IsAuthenticated, permissions.ClientPermissions)
    serializer_class = serializers.ClientsSerializer
    queryset = models.Client.objects.all()


class ContractViewset(ModelViewSet):

    permission_classes = (IsAuthenticated, permissions.ContractPermissions)
    serializer_class = serializers.ContractSerializer
    queryset = models.Contract.objects.all()


class EventViewset(ModelViewSet):

    permission_classes = (IsAuthenticated, permissions.EventPermissions)
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event_date']




