from rest_framework import serializers
from django.apps import apps
from .models import Ponuda


Kupac = apps.get_model("kupci", "Kupac")
Stan = apps.get_model("stanovi", "Stan")


class StanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stan
        fields = ('owner', 'buyer', 'advertised', 'district', 'address', 'lamella', 'size', 'floor', 'num_of_rooms',
                  'orientation', 'num_of_terraces', 'price', 'available', 'reserved', 'sold', 'image')


class PonudaSerializer(serializers.ModelSerializer):
    class Meta:
        stanovi = StanSerializer(many=True, read_only=True)
        model = Ponuda
        fields = '__all__'
