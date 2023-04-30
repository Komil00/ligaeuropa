from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Player, Club, Seasson, TournamentTable, Matches,\
      Game, AboutPlayer, GoalsPlayer,\
        YellowCardsPlayer,RedCardsPlayer,Like, Trophey
            #   Subject, Question, TestBought, Test, UserAnswer, TestResult

# admin.site.register(Subject)
# admin.site.register(Test)
# admin.site.register(Question)
# admin.site.register(TestBought)
# admin.site.register(UserAnswer)
# admin.site.register(TestResult)

# Register your models here.



class PlayerInline(admin.StackedInline):
    model = Player
    max_num = 12
    extra = 0

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image}" width="170" height="150" />')
        return ''

    image_tag.short_description = 'Фото игрока'

admin.site.register(Seasson)
admin.site.register(Trophey)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'player_count')
    list_display_links = ('name',)
    inlines = [PlayerInline]

    def image_tag(self, obj):
        from django.utils.html import format_html
        if obj.icon:
            return format_html('<img src="{}" width="100" height="80" />'.format(obj.icon.url))
        return ''

    image_tag.short_description = 'Эмблема'

    def player_count(self, obj):
        print(obj)
        return Player.objects.filter(club=obj.id).count()

    player_count.short_description = 'Кол-во игроков'


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'club',  'last_name', 'numb')
    list_display_links = ('first_name','club',  'numb')

# @admin.register(GoalsPlayer)
# class GoalsPlayerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'get_author_name', 'counts', 'get_author_club_name')
#     list_display_links = list_display

#     @admin.display(description='Author Name')
#     def get_author_name(self, obj):
#         return obj.player.first_name
#     @admin.display(description='Author lastname')
#     def counts(self, obj):
#         return obj.counts
#     @admin.display(description='Club Name')
#     def get_author_club_name(self, obj):
#         return obj.player.club.name


# @admin.register(RedCardsPlayer)
# class RedCardsPlayerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'get_author_name', 'redcard_count', 'get_author_club_name')
#     list_display_links = list_display

#     @admin.display(description='Author Name')
#     def get_author_name(self, obj):
#         return obj.player.first_name
#     @admin.display(description='Author lastname')
#     def redcard_count(self, obj):
#         return obj.counts
#     @admin.display(description='Club Name')
#     def get_author_club_name(self, obj):
#         return obj.player.club.name

# @admin.register(YellowCardsPlayer)
# class YellowCardsPlayerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'get_author_name', 'yellowcard_count', 'get_author_club_name')
#     list_display_links = list_display

#     @admin.display(description='Author Name')
#     def get_author_name(self, obj):
#         return obj.player.first_name
#     @admin.display(description='Author lastname')
#     def yellowcard_count(self, obj):
#         return obj.counts
#     @admin.display(description='Club Name')
#     def get_author_club_name(self, obj):
#         return obj.player.club.name

class GameInline(admin.StackedInline):
    model = Game
    extra = 0
    max_num = 1


@admin.register(TournamentTable)
class TournamentTableAdmin(admin.ModelAdmin):
    list_display = ('club', 'game', 'win', 'draw', 'lose', 'goals', 'missed_goals', 'diff', 'point')
    list_display_links = ('club', 'game', 'win', 'draw', 'lose', 'goals', 'missed_goals', 'diff', 'point')


@admin.register(Matches)
class TourAdmin(admin.ModelAdmin):
    list_display = ('tour', 'home', 'guest', 'date', 'finished')
    list_display_links = ('tour', 'home', 'guest', 'date')
    inlines = [GameInline, ]
    search_fields = ('home', 'guest')
    list_filter = ('home', 'guest', 'finished', 'date')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['tour', 'home_point', 'guest_point']
    list_display_links = list_display
    search_fields = ['tour']
    list_filter = ['tour']

# admin.site.register(Like)

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
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'info', 'interview_author', 'date']
    list_display_links = ['title', 'image_tag', 'interview_author', 'date']
    search_fields = ['title', 'interview_author', 'date']
    list_filter = ['title', 'interview_author', 'date']

    def image_tag(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" width="100" height="80" />'.format(obj.image.url))
        return ''

    image_tag.short_description = 'Фото'


    