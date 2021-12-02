from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from korisnici.models import Korisnik
from ponude.models import Ponuda
from .filters import StanByFilters
from .models import Stan
from .serializers import ProdavacSerializer, SamoStanSerializer, StanSerializer


class ProdavacStanList(generics.ListAPIView):
    """ lista vlasnika sa stanovima """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Korisnik.objects.all()
    serializer_class = ProdavacSerializer


class ProdavacStanDetail(generics.RetrieveAPIView):
    """ vlasnik po korisnickom imenu sa stanom/vima """

    permission_classes = [permissions.IsAdminUser]
    queryset = Korisnik.objects.all()
    serializer_class = ProdavacSerializer
    lookup_field = 'username'

    def myview(self, request):
        owner = [obj.korisnik for obj in Korisnik.objects.all()]
        return request, {'owner': owner}


class StanCreate(generics.CreateAPIView):
    """ kreiranje stana"""

    permission_classes = [permissions.IsAuthenticated]
    queryset = Stan.objects.all()
    serializer_class = SamoStanSerializer


class StanList(generics.ListAPIView):
    """ lista svih stanova """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Stan.objects.all()
    serializer_class = SamoStanSerializer


class StanDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    """ editabilni detalji stana po id-ju """

    permission_classes = [permissions.IsAdminUser]
    queryset = Stan.objects.all()
    serializer_class = SamoStanSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StanBy(viewsets.ModelViewSet):
    """ pretraga stanova po filterima """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Stan.objects.all()
    serializer_class = SamoStanSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StanByFilters

    @action(methods=['get'], detail=False)
    def my_set(self, request):
        my_set = self.get_queryset()
        serializer = self.get_serializer_class()(my_set)
        return Response(serializer.data)


class StanPonudeList(generics.ListAPIView):
    """ lista svih stanova sa ponudama"""

    permission_classes = [IsAuthenticated]
    queryset = Stan.objects.all()
    serializer_class = StanSerializer


class StanIdPonude(generics.ListAPIView):
    """ stan po id-ju sa ponudama """

    permission_classes = [IsAuthenticated]
    queryset = Stan.objects.all()
    serializer_class = StanSerializer
    lookup_field = 'id_stana'

    def get_queryset(self):
        queryset = Stan.objects.all()
        id_stana = self.kwargs['id_stana']
        if self.kwargs:
            queryset = queryset.filter(id_stana__icontains=id_stana)
        return queryset
