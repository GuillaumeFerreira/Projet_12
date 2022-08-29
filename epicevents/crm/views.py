from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models, serializers
import logging

logger = logging.getLogger(__name__)


class ClientsViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ClientsSerializer
    queryset = models.Client.objects.all()
    logger.info('test')


class ContractViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ContractSerializer
    queryset = models.Contract.objects.all()


class EventViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()