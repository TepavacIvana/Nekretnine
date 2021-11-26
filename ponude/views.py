from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Ponuda
from .serializers import *
from .filters import PonudaByFilters


class PonudaList(generics.ListCreateAPIView):
    """ lista svih ponuda """

    permission_classes = [IsAuthenticated]
    queryset = Ponuda.objects.all()
    serializer_class = PonudaSerializer


class PonudaDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
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

    @action(methods=['get'], detail=False)
    def my_set(self, request):
        my_set = self.get_queryset()
        serializer = self.get_serializer_class()(my_set)
        return Response(serializer.data)

