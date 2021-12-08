from rest_framework import serializers

from .models import Ponuda


class PonudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponuda
        fields = '__all__'
