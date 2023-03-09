from rest_framework.routers import DefaultRouter
from core.viewsets import MatchesViewSet, TournamentTableViewSet,\
      AboutPlayerViewSet, GamesViewSet, PlayerGoalViewSet,\
      NewsViewSet

router = DefaultRouter()

router.register('matches', MatchesViewSet, basename='matches')
router.register('table', TournamentTableViewSet, basename='tournament-table')
router.register('aboutplayer', AboutPlayerViewSet, basename='aboutplayer')
# router.register('games', GamesViewSet, basename='games')
router.register('playergoals', PlayerGoalViewSet, basename='playergoals')
router.register('news', NewsViewSet, basename='news')