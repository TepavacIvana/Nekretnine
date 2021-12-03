from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from stanovi.models import Stan
from .models import Ponuda
from .serializers import PonudaSerializer, OdobrenjeSerializer
from .filters import PonudaByFilters
from rest_framework.decorators import api_view


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
    """ editabilni detalji ponude po id-ju """

    permission_classes = [permissions.IsAdminUser]
    queryset = Ponuda.objects.all()
    serializer_class = PonudaSerializer

    def put(self, request, *args, **kwargs):



        id_ponude = kwargs['pk']
        id_stana = request.data['apartment']  # get ID Stana
        qurey_stan = Stan.objects.values('price').filter(id_stana=id_stana)  # Preuzmi obj Stan sa tim IDem
        cena_stana_prodavac = qurey_stan[0]['price']
        cena_stana_ponude = int(request.data['price_for_buyer'])

        qPonude = Ponuda.objects.values_list().filter(id_ponude=1)
        qPonude.update(approved=True)


        # print(type(cena_stana_prodavac))

        # print("cena_stana_prodavac")
        # print("###########################")
        # print(cena_stana_prodavac)

        # print("cena_stana_ponude")
        # print("###########################")
        # print(cena_stana_ponude)

        print('test')
        #Ponuda.objects.filter(id_ponude=1).update(note="TEST NOTE")

        # if cena_stana_prodavac == cena_stana_ponude:
        # else:
        #     print('NONO')

        return self.update(request, *args, **kwargs)

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

# class Odobrenje(generics.RetrieveUpdateAPIView):
#     queryset = Stan.objects.all()
#     # lookup_field = 'price'
#     p1 = [s.price for s in queryset]
#     a1 = [s.available for s in queryset]
#
#     queryset = Ponuda.objects.all()
#     # lookup_field = 'price_for_buyer'
#     p2 = [p.price_for_buyer for p in queryset]
#     s2 = [p.sales_status for p in queryset]
#     a2 = [p.approved for p in queryset]
#
#     if p1 == p2:
#         a1 = False
#         # s2 = s2.RESERVED
#         a2 = True
#     else:
#         message = {'Message': 'You have no approval'}


# class Odobrenje(generics.RetrieveUpdateAPIView):
#     queryset = Ponuda.objects.all()
#     serializer_class = OdobrenjeSerializer
#     lookup_field = 'id_ponude'
#     cena_stana_prodavac = [p.apartment.price for p in queryset]
#     dostupnost_stana = [p.apartment.available for p in queryset]
#
#     p2 = [p.price_for_buyer for p in queryset]
#     s2 = [p.sales_status for p in queryset]
#     a2 = [p.approved for p in queryset]
#
#     if cena_stana_prodavac == p2:
#         a1 = False
#         # s2 = s2.RESERVED
#         a2 = True
#     else:
#         message = {'Message': 'You have no approval'}
