from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Matches, TournamentTable, AboutPlayer, Game,\
      PlayerGoal, News
from .serializers import MatchesListSerializer, TournamentTableSerializer,\
      AboutPlayerSerializers, GameListSerializer, PlayerGoalSerializers,\
      NewsPutDeleteSerializer, NewsListSerializers


class MatchesViewSet(viewsets.ModelViewSet):
    queryset = Matches.objects.all().order_by('finished')
    serializer_class = MatchesListSerializer
    http_method_names = ('get', )
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('tour', 'home', 'guest')


class TournamentTableViewSet(viewsets.ModelViewSet):
    queryset = TournamentTable.objects.all().order_by('-point')
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

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers
    http_method_names = ('get', 'put', 'delete')

    # def get_serializer_class(self):
    #     if 