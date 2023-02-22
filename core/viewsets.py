from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Tour, TournamentTable
from .serializers import TourListSerializer, TournamentTableSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourListSerializer
    http_method_names = ('get', )
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('tour', 'home', 'guest')


class TournamentTableViewSet(viewsets.ModelViewSet):
    queryset = TournamentTable.objects.all()
    serializer_class = TournamentTableSerializer
    http_method_names = ('get', )
