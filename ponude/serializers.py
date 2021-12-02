from rest_framework import serializers

from stanovi.models import Stan
from .models import Ponuda


class PonudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponuda
        fields = '__all__'


