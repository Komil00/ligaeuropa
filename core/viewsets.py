from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets ,permissions, status
from .models import Club, Matches, TournamentTable, AboutPlayer, Game, News,\
      GoalsPlayer, YellowCardsPlayer,RedCardsPlayer, Like
from .serializers import MatchesListSerializer, TournamentTableSerializer,\
      AboutPlayerSerializers, GameListSerializer,\
      NewsPutDeleteSerializer, NewsListSerializers, GoalsPlayerSerializers,\
      RedCardsPlayerSerializers,YellowCardsPlayerSerializers, LikeSerializer,\
      ForClubSerializers
from rest_framework.response import Response
from rest_framework.decorators import action


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

# class InfoMatchViewSet(viewsets.ModelViewSet):
#     queryset = InfoMatch.objects.all()
#     serializer_class = InfoMatchSerializers
#     http_method_names = ('get')

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers
    http_method_names = ('get', 'put', 'delete')
    # permission_classes = (permissions.AllowAny)

    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class GoalsViewSet(viewsets.ModelViewSet):
    queryset = GoalsPlayer.objects.all().order_by('-counts')
    serializer_class = GoalsPlayerSerializers
    http_method_names = ('get')

class RedCardsViewSet(viewsets.ModelViewSet):
    queryset = RedCardsPlayer.objects.all().order_by('-counts')
    serializer_class = RedCardsPlayerSerializers
    http_method_names = ('get')

class YellowCardsViewSet(viewsets.ModelViewSet):
    queryset = YellowCardsPlayer.objects.all().order_by('-counts')
    serializer_class = YellowCardsPlayerSerializers
    http_method_names = ('get')



class LikeViewSet(viewsets.ViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = LikeSerializer(data=request.data)
        aboutplayer = AboutPlayer.objects.get(id=request.data['aboutplayer'])
        forlike = request.POST.get('is_like', False)
        if forlike:
            if aboutplayer.likes_count==None:
                aboutplayer.likes_count=0
                aboutplayer.save()
                aboutplayer.likes_count =int(aboutplayer.likes_count) + 1
            else:
                aboutplayer.likes_count =int(aboutplayer.likes_count) + 1

        serializer.is_valid(raise_exception=True)
        aboutplayer.save()
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ForClubSerializers
    http_method_names = ('get')
