from rest_framework import serializers
from django.apps import apps
from .models import Kupac


Stan = apps.get_model("stanovi", "Stan")


class KupacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kupac
        fields = ('full_or_company_name', 'citizen', 'company', 'email', 'phone_num', 'PIB_JMBG', 'address')


class KupacStanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stan
        fields = ('address',)


class Kupac2Serializer(serializers.ModelSerializer):
    stanovi = KupacStanSerializer(many=True, read_only=True)

    class Meta:
        model = Kupac
        fields = ('full_or_company_name', 'stanovi')


class StanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stan
        fields = ('owner', 'buyer', 'advertised', 'district', 'address', 'lamella', 'size', 'floor', 'num_of_rooms',
                  'orientation', 'num_of_terraces', 'price', 'available', 'reserved', 'sold', 'image')


class StanKupacSerializer(serializers.ModelSerializer):
    stanovi_set = StanSerializer(many=True)

    class Meta:
        model = Kupac
        fields = '__all__'

    def create(self, validated_data):
        stanovi_validated_data = validated_data.pop('stanovi_set')
        buyer = Kupac.objects.create(**validated_data)
        stanovi_set_serializer = self.fields['stanovi_set']
        for each in stanovi_validated_data:
            each['buyer'] = buyer
        stanovi = stanovi_set_serializer.create(stanovi_validated_data)
        return buyer
