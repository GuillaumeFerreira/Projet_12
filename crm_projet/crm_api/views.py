from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models, serializers, permissions

class ClientsViewset(ModelViewSet):

    permission_classes = [IsAuthenticated,permissions.ClientPermissions]
    serializer_class = serializers.ClientsSerializer
    queryset = models.Client.objects.all()

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

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ContractSerializer
    queryset = models.Contract.objects.all()


class EventViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
