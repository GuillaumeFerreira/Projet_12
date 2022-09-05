from django_filters import rest_framework as filters
from . import models


class ClientFilter(filters.FilterSet):
    class Meta:
        model = models.Client
        fields = [
            'first_name',
            'email',
        ]