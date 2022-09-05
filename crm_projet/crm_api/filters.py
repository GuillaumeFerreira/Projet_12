from django_filters import rest_framework as filters
from . import models


class ContractFilter(filters.FilterSet):

    first_name = filters.CharFilter(method='filter_not_empty')
    def client_first_name(self,):
        client_contract = models.Client.objects.filter(employee_contact=self.request.user)
        return client_contract.first_name


    class Meta:
        model = models.Contract
        fields = ['first_name','date_created','amount']