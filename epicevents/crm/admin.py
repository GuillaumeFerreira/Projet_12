from django.contrib import admin
from . import models


class ClientAdmin(admin.ModelAdmin):

    def has_change_permission(self, request,obj=None):
        if request.user.is_superuser:
            return True
        else:
            if request.user.role == "COMMERCIAL":
                return True
            else:
                return False


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            if request.user.role == "COMMERCIAL":
                return True
            else:
                return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            if request.user.role == "COMMERCIAL":
                return True
            else:
                return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:

            if request.user.role == "COMMERCIAL":
                return qs.filter(employee_contact=request.user)
            elif request.user.role == "SUPPORT":
                event = models.Event.objects.filter(employee_event=request.user)

                return qs.filter(id__in=event)
            else:
                return qs
        else:
            return qs


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "notes", "client", "employee_event")

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            if request.user.role == "SUPPORT":
                return True
            else:
                return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            if request.user.role in ("COMMERCIAL", "SUPPORT"):
                return True
            else:
                return False

    def has_module_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            try:
                if request.user.role in ("COMMERCIAL", "SUPPORT"):
                    return True
                else:
                    return False
            except:
                return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(employee_event=request.user)


class ContractAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            if request.user.role == "COMMERCIAL":
                return True
            else:
                return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            if request.user.role == "COMMERCIAL":
                return True
            else:
                return False

    # affichage sur page admin
    def has_module_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
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


class EmployeeAdmin(admin.ModelAdmin):


    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            if request.user.role == "MANAGER":
                return True
            else:
                return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            if request.user.role == "MANAGER":
                return True
            else:
                return False
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            if request.user.role == "MANAGER":
                return True
            else:
                return False

    def has_module_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            try:
                if request.user.role == "MANAGER":
                    return True
                else:
                    return False
            except:
                return False


admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Contract, ContractAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Employee, EmployeeAdmin)
