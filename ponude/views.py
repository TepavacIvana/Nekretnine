from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Ponuda
from .serializers import PonudaSerializer
from .filters import PonudaByFilters
from rest_framework.decorators import api_view
from stanovi.models import Stan


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

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
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
#fdgdfg
    @action(methods=['get'], detail=False)
    def my_set(self, request):
        my_set = self.get_queryset()
        serializer = self.get_serializer_class()(my_set)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def odobrenje(request):
    if request.method == 'POST':
        price1 = Ponuda.objects.all().filter('apartment')
