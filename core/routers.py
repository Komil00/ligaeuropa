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
router.register('goals', GoalsViewSet, basename='goals')
router.register('red_cards', RedCardsViewSet, basename='red_cards')
router.register('yellow_cards', YellowCardsViewSet, basename='yellow_cards')