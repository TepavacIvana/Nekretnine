from rest_framework import serializers

from stanovi.models import Stan
from korisnici.models import Korisnik
from ponude.models import Ponuda


class ProdavacStanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stan
        fields = ('address',)


class ProdavacSerializer(serializers.ModelSerializer):
    stanovi = ProdavacStanSerializer(many=True, read_only=True)

    class Meta:
        model = Korisnik
        fields = ('username', 'stanovi')


class SamoStanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stan
        fields = ('id_stana',
                  'owner',
                  'advertised',
                  'district',
                  'address',
                  'lamella',
                  'size',
                  'floor',
                  'num_of_rooms',
                  'orientation',
                  'num_of_terraces',
                  'price',
                  'available',
                  'image')


class StanProdavacSerializer(serializers.ModelSerializer):
    stanovi_set = SamoStanSerializer(many=True)

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


class ListaPonudaStanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponuda
        fields = (
            "id_ponude",
            "buyer",
            "sales_status",
            "price_for_buyer",
            "note",
            "contract_num",
            "contract_date",
            "prodaja_detail",
            "approved",
        )


class StanSerializer(serializers.ModelSerializer):
    lista_ponuda_stana = ListaPonudaStanaSerializer(many=True, read_only=True)

    class Meta:
        model = Stan
        fields = ('id_stana',
                  'owner',
                  'advertised',
                  'district',
                  'address',
                  'lamella',
                  'size',
                  'floor',
                  'num_of_rooms',
                  'orientation',
                  'num_of_terraces',
                  'price',
                  'available',
                  'image',
                  "lista_ponuda_stana",
                  )
