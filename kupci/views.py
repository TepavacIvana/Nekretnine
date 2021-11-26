from rest_framework import generics, mixins, permissions
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Kupac
from .serializers import KupacSerializer, Kupac2Serializer


class KupacList(generics.ListCreateAPIView):
    """ lista svih kupaca i kreiranje kupca"""

    permission_classes = [IsAuthenticated]
    queryset = Kupac.objects.all()
    serializer_class = KupacSerializer


class KupacByName(generics.ListAPIView):
    """ detalji kupca po imenu """

    permission_classes = [permissions.IsAdminUser]
    serializer_class = KupacSerializer

    def get_queryset(self):
        queryset = Kupac.objects.all()
        full_or_company_name = self.kwargs['full_or_company_name']
        if self.kwargs:
            queryset = queryset.filter(full_or_company_name__icontains=full_or_company_name)
        return queryset


class KupacStanList(generics.ListAPIView):
    """ lista kupaca sa stanovima """

    permission_classes = [IsAuthenticated]
    queryset = Kupac.objects.all()
    serializer_class = Kupac2Serializer


class KupacStanDetail(generics.RetrieveAPIView):
    """ kupac po imenu sa stanom/vima """

    permission_classes = [permissions.IsAdminUser]
    queryset = Kupac.objects.all()
    serializer_class = Kupac2Serializer
    lookup_field = 'full_or_company_name'

    def myview(self, request):
        buyer = [obj.kupac for obj in Kupac.objects.all()]
        return request, {'buyer': buyer}

