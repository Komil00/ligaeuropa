from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.

class TeamInline(admin.StackedInline):
    model = Team
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
    inlines = [TeamInline, ]

    def image_tag(self, obj):
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon}" width="170" height="150" />')
        return ''

    image_tag.short_description = 'Эмблема'

    def player_count(self, obj):
        return Team.objects.filter(club=obj.id).count()

    player_count.short_description = 'Кол-во игроков'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('club', 'name', 'numb')
    list_display_links = ('club', 'name', 'numb')


class GameInline(admin.StackedInline):
    model = Game
    extra = 0
    max_num = 1


@admin.register(TournamentTable)
class TournamentTableAdmin(admin.ModelAdmin):
    list_display = ('club', 'game', 'win', 'draw', 'lose', 'goals', 'missed_goals', 'diff', 'point')
    list_display_links = ('club', 'game', 'win', 'draw', 'lose', 'goals', 'missed_goals', 'diff', 'point')


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('tour', 'home', 'guest', 'date', 'finished')
    list_display_links = ('tour', 'home', 'guest', 'date')
    inlines = [GameInline, ]
    search_fields = ('home', 'guest')
    list_filter = ('home', 'guest', 'finished', 'date')
