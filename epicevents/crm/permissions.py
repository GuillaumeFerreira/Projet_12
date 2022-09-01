from rest_framework import permissions
from . import models

class ClientPermissions(permissions.BasePermission):
    #permissions list
    def has_permission(self, request, view):
        # Utilisation de permissions.SAFE_METHODS, is a tuple containing 'GET', 'OPTIONS' and 'HEAD'
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user.role in ["MANAGER","COMMERCIAL"]:
                return True
            else:
                return False
    #permission detail
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user.role == "SUPPORT":
                event = models.Event.objects.filter(employee_event=request.user)
                return obj == event
            if request.user.role == "COMMERCIAL":
                return request.user == obj.employee_contact
            else:
                return True
        elif request.method == "POST":
            if request.user.role == "SUPPORT":
                return False
            else:
                return True
        else:
            if request.user.role == "COMMERCIAL":
                return request.user == obj.employee_contact
            elif request.user.role == "SUPPORT":
                return False
            else:
                return True




class ContractPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ["PUT", "PATCH"]:
            return request.user.role == "COMMERCIAL"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.employee_contact == request.user


class EventPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ("PUT", "PATCH"):
            return request.user.role in ("COMMERCIAL", "SUPPORT")
        return request.user.role == "COMMERCIAL"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.employee_event == request.user
