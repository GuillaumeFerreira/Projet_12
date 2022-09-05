from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models, serializers, permissions, filters
import django_filters.rest_framework
#import logging

#logger = logging.getLogger(__name__)


class ClientsViewset(ModelViewSet):

    permission_classes = [IsAuthenticated,permissions.ClientPermissions]
    serializer_class = serializers.ClientsSerializer
    queryset = models.Client.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['first_name','email']

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.method == "GET":
            if self.request.user.groups.filter(name='SUPPORT').exists():
                contracts = models.Event.objects.filter(employee_event=self.request.user)
                clients = models.Contract.objects.filter(id__in=contracts)
                return queryset.filter(id__in=clients)
            elif self.request.user.groups.filter(name='COMMERCIAL').exists():
                return queryset.filter(employee_contact=self.request.user)
            elif self.request.user.groups.filter(name='MANAGER').exists():
                return queryset
            else:
                return queryset



class ContractViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, permissions.ContractPermissions]
    serializer_class = serializers.ContractSerializer
    queryset = models.Contract.objects.all()

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['client','date_created','amount']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method == "GET":
            if self.request.user.groups.filter(name='COMMERCIAL').exists():
                return queryset.filter(employee_contact=self.request.user)
            else:
                return queryset

class EventViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, permissions.EventPermissions]
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.method == "GET":
            if self.request.user.groups.filter(name='SUPPORT').exists():
                return queryset.filter(employee_event=self.request.user)
            elif self.request.user.groups.filter(name='COMMERCIAL').exists():
                client_contract = models.Client.objects.filter(employee_contact=self.request.user)
                contract_event = models.Contract.objects.filter(client_id__in=client_contract)
                events = models.Event.objects.filter(contract_id__in=contract_event)
                return queryset.filter(id__in=events)
            elif self.request.user.groups.filter(name='MANAGER').exists():
                return queryset
            else:
                return queryset