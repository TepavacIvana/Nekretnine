from rest_framework import serializers

from stanovi.models import Stan
from .models import Ponuda
from django.utils.text import slugify


class PonudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponuda
        fields = '__all__'


class OdobrenjeSerializer(serializers.ModelSerializer):
    apartment_price_slug = serializers.SerializerMethodField()

    def get_apartment_price_slug(self, instance):
        return slugify(instance.apartment.price)

    class Meta:
        model = Ponuda
        fields = ('apartment_price_slug', 'price_for_buyer', 'sales_status', 'approved')

