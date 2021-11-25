from rest_framework import serializers
from django.apps import apps
from .models import Stan

Korisnik = apps.get_model("korisnici", "Korisnik")


class KorisnikStanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stan
        fields = ('address',)


class KorisnikSerializer(serializers.ModelSerializer):
    stanovi = KorisnikStanSerializer(many=True, read_only=True)

    class Meta:
        model = Korisnik
        fields = ('username', 'stanovi')


class StanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stan
        fields = ('owner', 'buyer', 'advertised', 'district', 'address', 'lamella', 'size', 'floor', 'num_of_rooms',
                  'orientation', 'num_of_terraces', 'price', 'available', 'reserved', 'sold', 'image')


class StanKorisnikSerializer(serializers.ModelSerializer):
    stanovi_set = StanSerializer(many=True)

    class Meta:
        model = Korisnik
        fields = '__all__'

    def create(self, validated_data):
        stanovi_validated_data = validated_data.pop('stanovi_set')
        owner = Korisnik.objects.create(**validated_data)
        stanovi_set_serializer = self.fields['stanovi_set']
        for each in stanovi_validated_data:
            each['owner'] = owner
        stanovi = stanovi_set_serializer.create(stanovi_validated_data)
        return owner
