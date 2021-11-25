from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, permissions, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Stan
from .serializers import *
from .filters import StanByFilters
from .permissions import IsKorisnikOwner


class KorisnikStanList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Korisnik.objects.all()
    serializer_class = KorisnikSerializer


class KorisnikStanDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Korisnik.objects.all()
    serializer_class = KorisnikSerializer
    lookup_field = 'username'

    def myview(self, request):
        owner = [obj.korisnik for obj in Korisnik.objects.all()]
        return request, {'owner': owner}


class StanList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Stan.objects.all()
    serializer_class = StanSerializer


class StanDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Stan.objects.all()
    serializer_class = StanSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StanBy(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Stan.objects.all()
    serializer_class = StanSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StanByFilters

    @action(methods=['get'], detail=False)
    def my_set(self, request):
        my_set = self.get_queryset()
        serializer = self.get_serializer_class()(my_set)
        return Response(serializer.data)

