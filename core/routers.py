from rest_framework.routers import DefaultRouter
from core.viewsets import MatchesViewSet, TournamentTableViewSet,\
      AboutPlayerViewSet, GamesViewSet, NewsViewSet,\
            GoalsViewSet, YellowCardsViewSet, RedCardsViewSet

router = DefaultRouter()

router.register('matches', MatchesViewSet, basename='matches')
router.register('table', TournamentTableViewSet, basename='tournament-table')
router.register('aboutplayer', AboutPlayerViewSet, basename='aboutplayer')
# router.register('games', GamesViewSet, basename='games')
# router.register('infomatch', InfoMatchViewSet, basename='infomatch')
router.register('news', NewsViewSet, basename='news')
router.register('scorers', GoalsViewSet, basename='scorers')
router.register('stat_red_cards', RedCardsViewSet, basename='stat_red_cards')
router.register('stat_yellow_cards', YellowCardsViewSet, basename='stat_yellow_cards')