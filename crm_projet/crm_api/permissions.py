from rest_framework import permissions
from . import models


class ClientPermissions(permissions.BasePermission):
    #permissions list
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        else:
            if request.user.groups.filter(name='SUPPORT').exists():
                return False
            elif request.user.groups.filter(name='MANAGER').exists():
                return True
            elif request.user.groups.filter(name='MANAGER').exists():
                return True
            else:
                return False
    #permission detail
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            if request.user.groups.filter(name='SUPPORT').exists():
                event = models.Event.objects.filter(employee_event=request.user)
                return obj == event
            elif request.user.groups.filter(name='COMMERCIAL').exists():
                return request.user == obj.employee_contact
            elif request.user.groups.filter(name='MANAGER').exists():
                return True
            else:
                return False
        elif request.method == "POST":
            if request.user.groups.filter(name='SUPPORT').exists():
                return False
            elif request.user.groups.filter(name='COMMERCIAL').exists():
                return True
            elif request.user.groups.filter(name='MANAGER').exists():
                return True
            else:
                return False
        else:
            if request.user.groups.filter(name='COMMERCIAL').exists():
                return request.user == obj.employee_contact
            elif request.user.groups.filter(name='SUPPORT').exists():
                return False
            elif request.user.groups.filter(name='MANAGER').exists():
                return True
            else:
                return False


class ContractPermissions(permissions.BasePermission):
    #permissions list
    def has_permission(self, request, view):
        if request.user.groups.filter(name='SUPPORT').exists():
            return False
        elif request.user.groups.filter(name='COMMERCIAL').exists():
             return True
        elif request.user.groups.filter(name='MANAGER').exists():
            return True
        else:
            return False

    #permission detail
    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            if request.user.groups.filter(name='SUPPORT').exists():
                return False
            elif request.user.groups.filter(name='COMMERCIAL').exists():
                return True
            elif request.user.groups.filter(name='MANAGER').exists():
                return True
            else:
                return False
        else:
            if request.user.groups.filter(name='COMMERCIAL').exists():
                return request.user == obj.employee_contact
            elif request.user.groups.filter(name='SUPPORT').exists():
                return False
            elif request.user.groups.filter(name='MANAGER').exists():
                return True
            else:
                return False