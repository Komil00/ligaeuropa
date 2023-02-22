from django.contrib import admin
from .models import *


# Register your models here.


class GameInline(admin.StackedInline):
    model = Game
    extra = 0
    max_num = 1


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('tour', 'home', 'guest', 'date', 'finished')
    list_display_links = ('tour', 'home', 'guest', 'date')
    inlines = [GameInline, ]
    search_fields = ('home', 'guest')
    list_filter = ('home', 'guest', 'finished', 'date')
