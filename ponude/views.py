from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from stanovi.models import Stan
from .models import Ponuda
from .serializers import PonudaSerializer
from .filters import PonudaByFilters


class PonudaCreate(generics.CreateAPIView):
    """ kreiranje ponude """

    permission_classes = [IsAuthenticated]
    queryset = Ponuda.objects.all()
    serializer_class = PonudaSerializer


class PonudaList(generics.ListAPIView):
    """ lista svih ponuda """

    permission_classes = [IsAuthenticated]
    queryset = Ponuda.objects.all()
    serializer_class = PonudaSerializer


class PonudaDetail(generics.RetrieveUpdateDestroyAPIView):
    """ editabilni detalji ponude po id-ju i odobrenja """

    permission_classes = [permissions.IsAdminUser]
    queryset = Ponuda.objects.all()
    serializer_class = PonudaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        id_ponude = kwargs['pk']
        id_stana = request.data['apartment']
        query_stan = Stan.objects.values('price').filter(id_stana=id_stana)
        query2_stan = Stan.objects.values('available').filter(id_stana=id_stana)
        cena_stana_prodavac = query_stan[0]['price']
        cena_stana_ponude = int(request.data['price_for_buyer'])

        if cena_stana_prodavac == cena_stana_ponude:
            ponuda = Ponuda.objects.filter(id_ponude=id_ponude)
            ponuda.update(approved=True)
            query2_stan.update(available=False)
            ponuda.update(sales_status='reserved')

            return Response('You have approval')
        else:
            return Response('You have no approval')

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PonudaBy(viewsets.ModelViewSet):
    """ pretraga ponuda po filterima """

    permission_classes = [IsAuthenticated]
    queryset = Ponuda.objects.all()
    serializer_class = PonudaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PonudaByFilters

    @action(methods=['get'], detail=False)
    def my_set(self, request):
        my_set = self.get_queryset()
        serializer = self.get_serializer_class()(my_set)
        return Response(serializer.data)
