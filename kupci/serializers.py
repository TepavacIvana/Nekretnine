from rest_framework import serializers

from ponude.models import Ponuda
from .models import Kupac


class ListaPonudaKupcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponuda
        fields = (
            "id_ponude",
            "apartment",
            "sales_status",
            "price_for_buyer",
            "note",
            "contract_num",
            "contract_date",
            "prodaja_detail",
            "approved",
        )


class KupacSerializer(serializers.ModelSerializer):
    lista_ponuda_kupca = ListaPonudaKupcaSerializer(many=True, read_only=True)

    class Meta:
        model = Kupac
        fields = ('id_kupca',
                  'full_or_company_name',
                  'status_buyer',
                  'email',
                  'phone_num',
                  'PIB_JMBG',
                  'address',
                  "lista_ponuda_kupca",
                  )


class SamoKupacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kupac
        fields = '__all__'
