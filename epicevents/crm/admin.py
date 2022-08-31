from django.contrib import admin
from . import models
from django.urls import reverse



class EventAdmin(admin.ModelAdmin):
    list_display = ('id',  'notes', 'client', 'employee_event')
    def has_change_permission(self, request):
        if request.user.role == "SUPPORT":
            return True
        else:
            return False
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(employee_event=request.user)

class ContractAdmin(admin.ModelAdmin):

    #affichage sur page admin
    def has_change_permission(self, request):

        if request.user.role == "COMMERCIAL":
            return True
        else:
            return False

    def has_module_permission(self,request):
        try:
            if request.user.role == "COMMERCIAL":
                return True
            else:
                return False
        except:
            return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(employee_contact=request.user)

admin.site.register(models.Client)
admin.site.register(models.Contract,ContractAdmin)
admin.site.register(models.Event,EventAdmin)
admin.site.register(models.Employee)
