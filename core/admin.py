from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Player, Club, TournamentTable, Tour, AboutPlayer


# Register your models here.



class PlayerInline(admin.StackedInline):
    model = Player
    extra = 0

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image}" width="170" height="150" />')
        return ''

    image_tag.short_description = 'Фото игрока'


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'player_count')
    list_display_links = ('name',)
    inlines = [PlayerInline, ]

    def image_tag(self, obj):
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon}" width="170" height="150" />')
        return ''

    image_tag.short_description = 'Эмблема'

    def player_count(self, obj):
        return Player.objects.filter(club=obj.id).count()

    player_count.short_description = 'Кол-во игроков'


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'club',  'last_name', 'numb')
    list_display_links = ('first_name','club',  'numb')


# class GameInline(admin.StackedInline):
#     model = Game
#     extra = 0
#     max_num = 1


@admin.register(TournamentTable)
class TournamentTableAdmin(admin.ModelAdmin):
    list_display = ('club', 'game', 'win', 'draw', 'lose', 'goals', 'missed_goals', 'diff', 'point')
    list_display_links = ('club', 'game', 'win', 'draw', 'lose', 'goals', 'missed_goals', 'diff', 'point')


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('tour', 'home', 'guest', 'date', 'finished')
    list_display_links = ('tour', 'home', 'guest', 'date')
    # inlines = [GameInline, ]
    search_fields = ('home', 'guest')
    list_filter = ('home', 'guest', 'finished', 'date')

# admin.site.register(Game)
# admin.site.register(PlayerGoal)

# admin.site.register(AboutPlayer)

@admin.register(AboutPlayer)
class AboutPlayerAdmin(admin.ModelAdmin):
    list_display = ['get_author_name','get_author_last_name', 'get_author_club_name', 'age']
    list_display_links = list_display
    # search_fields = ['player__first_name', 'player__last_name']
    # list_filter = ['player__lastname']
    @admin.display(description='Author Name')
    def get_author_name(self, obj):
        return obj.player.first_name
    @admin.display(description='Author lastname')
    def get_author_last_name(self, obj):
        return obj.player.last_name
    @admin.display(description='Club Name')
    def get_author_club_name(self, obj):
        return obj.player.club.name