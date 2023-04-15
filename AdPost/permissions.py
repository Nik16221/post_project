from django.core.exceptions import ValidationError
from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, obj, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.login == request.user.login
