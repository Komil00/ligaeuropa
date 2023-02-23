from rest_framework import serializers
from .models import Tour, Club, TournamentTable, Game


class ClubForTourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('home_point', 'guest_point', 'red_card', 'yellow_card', 'link')


class TourListSerializer(serializers.ModelSerializer):
    home = ClubForTourListSerializer(read_only=True)
    guest = ClubForTourListSerializer(read_only=True)
    details = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = '__all__'

    def get_details(self, detail):
        if Game.objects.filter(tour=detail.id).exists():
            game = Game.objects.get(tour=detail.id)
            return {
                'home_point': game.home_point,
                'guest_point': game.guest_point,
                'red_card': game.red_card,
                'yellow_card': game.yellow_card,
            }
        return {}


class TournamentTableSerializer(serializers.ModelSerializer):
    club = ClubForTourListSerializer(read_only=True)

    class Meta:
        model = TournamentTable
        fields = "__all__"
