from django.contrib import admin

from digitalAdventures.posts.models import ImagePost


@admin.register(ImagePost)
class PostAdmin(admin.ModelAdmin):
    pass
