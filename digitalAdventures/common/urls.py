from django.urls import path

from digitalAdventures.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
