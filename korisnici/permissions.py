from rest_framework import permissions


class IsKorisnikOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsFinancesMember(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'Finansije'

