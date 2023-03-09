from rest_framework.routers import DefaultRouter
from core.viewsets import TourViewSet, TournamentTableViewSet,\
      AboutPlayerViewSet, GamesViewSet, PlayerGoalViewSet

router = DefaultRouter()

router.register('tour', TourViewSet, basename='tour')
router.register('table', TournamentTableViewSet, basename='tournament-table')
router.register('aboutplayer', AboutPlayerViewSet, basename='aboutplayer')
router.register('games', GamesViewSet, basename='games')
router.register('playergoals', PlayerGoalViewSet, basename='playergoals')