from rest_framework import serializers
from .models import Matches, Club, News, TournamentTable,\
      Game, AboutPlayer, Player,\
      GoalsPlayer,RedCardsPlayer,YellowCardsPlayer


class ClubForTourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class MatchesListSerializer(serializers.ModelSerializer):
    home = ClubForTourListSerializer(read_only=True)
    guest = ClubForTourListSerializer(read_only=True)
    details = serializers.SerializerMethodField()

    class Meta:
        model = Matches
        fields = '__all__'
        # exclude = ['date'] 

    def get_details(self, detail):
        if Game.objects.filter(tour=detail.id).exists():
            game = Game.objects.get(tour=detail.id)
            return {
                'tour': game.tour.tour,
                'home_point': game.home_point,
                'guest_point': game.guest_point,
                'link': game.link,
                'home_red_card': game.home_red_card,
                'guest_red_card': game.guest_red_card,
                'home_yellow_card': game.home_yellow_card,
                'guest_yellow_card': game.guest_yellow_card,
            }
        return {}

class GameListSerializer(serializers.ModelSerializer):
    tour = MatchesListSerializer()
    class Meta:
        model = Game
        fields = '__all__'

    def get_details(self, detail):
        if Game.objects.filter(tour=detail.id).exists():
            game = Game.objects.get(tour=detail.id)
            return {
                'home_point': game.home_point,
                'guest_point': game.guest_point,
                'link': game.link,
                'home_red_card': game.home_red_card,
                'guest_red_card': game.guest_red_card,
                'home_yellow_card': game.home_yellow_card,
                'guest_yellow_card': game.guest_yellow_card,
            }
        return {}


class TournamentTableSerializer(serializers.ModelSerializer):
    club = ClubForTourListSerializer(read_only=True)

    class Meta:
        model = TournamentTable
        fields = "__all__"

class PlayerSerializers(serializers.ModelSerializer):
    club = ClubForTourListSerializer()
    class Meta:
        model = Player
        fields = '__all__'

class AboutPlayerSerializers(serializers.ModelSerializer):
    player = PlayerSerializers()
    class Meta:
        model = AboutPlayer
        fields = '__all__'

class PlayerPlayerGoalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name']

class GamePlayerGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['tour']

class ClubForInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name']


# class InfoMatchSerializers(serializers.ModelSerializer):
    # player = PlayerPlayerGoalSerializers()
#     game = GamePlayerGoalSerializer()
#     player_command = ClubForInfoListSerializer()

#     class Meta:
#         model = InfoMatch
#         fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['player_command'] = instance.player.()
    #     return representation
    

class NewsPutDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NewsListSerializers(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'

class GoalsPlayerClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name', 'icon']

class PlayerforSerializers(serializers.ModelSerializer):
    club = GoalsPlayerClubSerializer()
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'image' , 'club']
        depth = 1

class GoalsPlayerSerializers(serializers.ModelSerializer):
    player = PlayerforSerializers()

    class Meta:
        model = GoalsPlayer
        fields = ['id', 'player', 'goals']

class RedCardsPlayerSerializers(serializers.ModelSerializer):
    player = PlayerforSerializers()

    class Meta:
        model = RedCardsPlayer
        fields = ['player', 'counts']

class YellowCardsPlayerSerializers(serializers.ModelSerializer):
    player = PlayerforSerializers()

    class Meta:
        model = YellowCardsPlayer
        fields = ['player', 'counts']