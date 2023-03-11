from rest_framework.routers import DefaultRouter
from core.viewsets import InfoMatchViewSet, MatchesViewSet, TournamentTableViewSet,\
      AboutPlayerViewSet, GamesViewSet,\
      NewsViewSet

router = DefaultRouter()

router.register('matches', MatchesViewSet, basename='matches')
router.register('table', TournamentTableViewSet, basename='tournament-table')
router.register('aboutplayer', AboutPlayerViewSet, basename='aboutplayer')
# router.register('games', GamesViewSet, basename='games')
router.register('infomatch', InfoMatchViewSet, basename='infomatch')
router.register('news', NewsViewSet, basename='news')