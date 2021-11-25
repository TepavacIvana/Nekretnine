from rest_framework import serializers
from django.apps import apps
from .models import Ponuda
from django.db.models.functions import Cast
from django.db.models import IntegerField


Kupac = apps.get_model("kupci", "Kupac")
Stan = apps.get_model("stanovi", "Stan")


class StanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stan
        fields = ('owner', 'buyer', 'advertised', 'district', 'address', 'lamella', 'size', 'floor', 'num_of_rooms',
                  'orientation', 'num_of_terraces', 'price', 'available', 'reserved', 'sold', 'image')


class PonudaSerializer(serializers.ModelSerializer):
    # discount = Stan['price'] - Ponuda['price_for_buyer']
    # stan = Stan.objects.all()
    # for s in stan:
    #     price1 = s.objects.annotate(as_integer=Cast('price', IntegerField())).get()
    #     value1 = price1.as_integer
    #     ponuda = Ponuda.objects.all()
    #     for p in ponuda:
    #         price2 = p.objects.annotate(as_integer=Cast('price_for_buyer', IntegerField())).get()
    #         value2 = price2.as_integer
    #         discount = value1 - value2

    # stan = Stan.objects.filter('price')
    # ponuda = Ponuda.objects.filter('price_for_buyer')
    # for s in stan:
    #     # value1 = s
    #     for p in ponuda:
    #         # value2 = p
    #         # if value1 > value2:
    #         if s > p:
    #             discount = s - p
    #         else:
    #             discount = p - s

    class Meta:
        stanovi = StanSerializer(many=True, read_only=True)
        model = Ponuda
        fields = '__all__'
