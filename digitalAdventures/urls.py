from django.contrib import admin
from django.urls import path, include
from digitalAdventures import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('digitalAdventures.common.urls')),
    path('games/', include('digitalAdventures.games.urls')),
    path('accounts/', include('digitalAdventures.accounts.urls')),
    path('posts/', include('digitalAdventures.posts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
