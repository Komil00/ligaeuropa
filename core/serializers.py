from rest_framework import serializers
from .models import Tour, Club, TournamentTable


class ClubForTourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class TourListSerializer(serializers.ModelSerializer):
    home = ClubForTourListSerializer(read_only=True)
    guest = ClubForTourListSerializer(read_only=True)

    class Meta:
        model = Tour
        fields = '__all__'


class TournamentTableSerializer(serializers.ModelSerializer):
    club = ClubForTourListSerializer(read_only=True)

    class Meta:
        model = TournamentTable
        fields = "__all__"


