from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from . import models, serializers, permissions
from rest_framework import status, viewsets, filters

# import logging

# logger = logging.getLogger(__name__)


class ClientsViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, permissions.ClientPermissions]
    serializer_class = serializers.ClientsSerializer
    queryset = models.Client.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["first_name", "email"]

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.method == "GET":
            if self.request.user.groups.filter(name="SUPPORT").exists():
                contracts = models.Event.objects.filter(
                    employee_event=self.request.user
                )
                clients = models.Contract.objects.filter(id__in=contracts)
                return queryset.filter(id__in=clients)
            elif self.request.user.groups.filter(name="COMMERCIAL").exists():
                return queryset.filter(employee_contact=self.request.user)
            elif self.request.user.groups.filter(name="MANAGER").exists():
                return queryset
            else:
                return queryset


class ContractViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, permissions.ContractPermissions]
    serializer_class = serializers.ContractSerializer
    queryset = models.Contract.objects.all()

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # search_fields = ['client__first_name','date_created','amount']
    filterset_fields = [
        "client__first_name",
        "client__email",
        "date_created",
        "amount",
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method == "GET":
            if self.request.user.groups.filter(name="COMMERCIAL").exists():
                return queryset.filter(employee_contact=self.request.user)
            else:
                return queryset


class EventViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, permissions.EventPermissions]
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = [
        "contract__client__first_name",
        "contract__client__email",
        "event_date",
    ]

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.method == "GET":
            if self.request.user.groups.filter(name="SUPPORT").exists():
                return queryset.filter(employee_event=self.request.user)
            elif self.request.user.groups.filter(name="COMMERCIAL").exists():
                client_contract = models.Client.objects.filter(
                    employee_contact=self.request.user
                )
                contract_event = models.Contract.objects.filter(
                    client_id__in=client_contract
                )
                events = models.Event.objects.filter(contract_id__in=contract_event)
                return queryset.filter(id__in=events)
            elif self.request.user.groups.filter(name="MANAGER").exists():
                return queryset
            else:
                return queryset
