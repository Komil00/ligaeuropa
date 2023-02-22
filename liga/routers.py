from rest_framework.routers import DefaultRouter
from core.viewsets import TourViewSet, TournamentTableViewSet

router = DefaultRouter()

router.register('matches', TourViewSet, basename='matches')
router.register('table', TournamentTableViewSet, basename='tournament-table')