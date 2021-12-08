from django.contrib.auth.models import BaseUserManager

from rest_framework.authtoken.models import Token
from rest_framework import serializers

from .models import Korisnik


class KorisnikRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Korisnik
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'password2', 'role')

    def validate_username(self, value):
        korisnik = Korisnik.objects.filter(username=value)
        if korisnik:
            raise serializers.ValidationError("Username is already taken")
        return value

    def validate_email(self, value):
        korisnik = Korisnik.objects.filter(email=value)
        if korisnik:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        data = self.get_initial()
        password = data.get('password2')
        password2 = value
        if password != password2:
            raise serializers.ValidationError('Passwords must match')
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get('password')
        password2 = value
        if password != password2:
            raise serializers.ValidationError('Passwords must match')
        return value


class KorisnikLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = Korisnik
        fields = ('id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'auth_token')
        read_only_fields = ('id', 'is_active', 'is_staff')

    def get_auth_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key


class EmptySerializer(serializers.Serializer):
    pass


class KorisnikListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'role')


class KorisnikDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = ('first_name', 'last_name', 'username', 'password', 'password2', 'role')
