from rest_framework import permissions


class ClientPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Utilisation de permissions.SAFE_METHODS, is a tuple containing 'GET', 'OPTIONS' and 'HEAD'
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == "COMMERCIAL"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.employee_contact


class ContractPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ("PUT", "PATCH"):
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
