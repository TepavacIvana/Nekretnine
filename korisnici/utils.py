from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers


def create_user_account(username, email, password, first_name="", last_name="", **extra_fields):
    korisnik = get_user_model().objects.create_user(
        username=username, email=email, password=password, first_name=first_name, last_name=last_name, **extra_fields
    )
    return korisnik


def get_and_authenticate_user(username, password):
    korisnik = authenticate(username=username, password=password)
    if korisnik is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return korisnik
