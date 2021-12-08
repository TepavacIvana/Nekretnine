from rest_framework import permissions, exceptions

from korisnici.models import Korisnik


class IsKorisnikOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsFinancesMember(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'Finansije'

