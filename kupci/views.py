from rest_framework import generics, mixins, permissions
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Kupac
from .serializers import KupacSerializer, SamoKupacSerializer


class KupacCreate(generics.CreateAPIView):
    """ kreiranje kupca """

    permission_classes = [IsAuthenticated]
    queryset = Kupac.objects.all()
    serializer_class = SamoKupacSerializer


class KupacList(generics.ListAPIView):
    """ lista svih kupaca """

    permission_classes = [IsAuthenticated]
    queryset = Kupac.objects.all()
    serializer_class = SamoKupacSerializer


class KupacByName(generics.ListAPIView):
    """ detalji kupca po imenu """

    permission_classes = [permissions.IsAdminUser]
    serializer_class = SamoKupacSerializer

    def get_queryset(self):
        queryset = Kupac.objects.all()
        full_or_company_name = self.kwargs['full_or_company_name']
        if self.kwargs:
            queryset = queryset.filter(full_or_company_name__icontains=full_or_company_name)
        return queryset


class KupacPonudeList(generics.ListAPIView):
    """ lista svih kupaca sa ponudama """

    permission_classes = [IsAuthenticated]
    queryset = Kupac.objects.all()
    serializer_class = KupacSerializer


class KupacIdPonude(generics.ListAPIView):
    """ kupac po id-ju sa ponudama """

    permission_classes = [IsAuthenticated]
    queryset = Kupac.objects.all()
    serializer_class = KupacSerializer
    lookup_field = 'id_kupca'

    def get_queryset(self):
        queryset = Kupac.objects.all()
        id_kupca = self.kwargs['id_kupca']
        if self.kwargs:
            queryset = queryset.filter(id_kupca__icontains=id_kupca)
        return queryset

