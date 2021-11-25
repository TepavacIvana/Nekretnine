from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status, generics, permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from . import serializers
from .utils import get_and_authenticate_user, create_user_account
from .serializers import KorisnikListSerializer, KorisnikDetailSerializer, AuthUserSerializer
from .permissions import IsKorisnikOwner
from .models import Korisnik


class AuthViewSet(viewsets.GenericViewSet):
    queryset = ''
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.KorisnikLoginSerializer,
        'register': serializers.KorisnikRegisterSerializer
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        korisnik = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(korisnik).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        korisnik = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(korisnik).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()


class KorisnikList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Korisnik.objects.all().order_by('-id')
    serializer_class = KorisnikListSerializer


class KorisnikDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsKorisnikOwner | permissions.IsAdminUser]
    queryset = Korisnik.objects.all()
    serializer_class = KorisnikDetailSerializer
    lookup_field = 'username'
