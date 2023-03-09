from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Matches, TournamentTable, AboutPlayer, Game, PlayerGoal
from .serializers import MatchesListSerializer, TournamentTableSerializer,\
      AboutPlayerSerializers, GameListSerializer, PlayerGoalSerializers


class MatchesViewSet(viewsets.ModelViewSet):
    queryset = Matches.objects.all()
    serializer_class = MatchesListSerializer
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

class GamesViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    http_method_names = ('get')

class PlayerGoalViewSet(viewsets.ModelViewSet):
    queryset = PlayerGoal.objects.all()
    serializer_class = PlayerGoalSerializers
    http_method_names = ('get')