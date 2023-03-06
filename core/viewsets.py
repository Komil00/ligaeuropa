from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Tour, TournamentTable, AboutPlayer
from .serializers import TourListSerializer, TournamentTableSerializer, AboutPlayerSerializers


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

class AboutPlayerViewSet(viewsets.ModelViewSet):
    queryset = AboutPlayer.objects.all()
    serializer_class = AboutPlayerSerializers
    http_method_names = ('get')