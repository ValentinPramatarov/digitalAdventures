from django.contrib import admin
from digitalAdventures.games.models import Game, Genre, Device


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass
