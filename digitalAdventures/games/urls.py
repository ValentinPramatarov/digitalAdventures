from django.urls import path, include

from digitalAdventures.games.views import create_game, GameDetailsView, GameEditView, GameDeleteView, GenreAddView, \
    GenreDeleteView, GenreEditView, GenreDetailsView, DeviceAddView, DeviceDetailsView, DeviceEditView, DeviceDeleteView

urlpatterns = (
    path('add/', create_game, name='game add'),
    path('<int:pk>/', include([
        path('details/', GameDetailsView.as_view(), name='game details'),
        path('edit/', GameEditView.as_view(), name='game edit'),
        path('delete/', GameDeleteView.as_view(), name='game delete'),
    ])),
    path('genre/add/', GenreAddView.as_view(), name='genre add'),
    path('genre/<int:pk>/', include([
        path('details/', GenreDetailsView.as_view(), name='genre details'),
        path('edit/', GenreEditView.as_view(), name='genre edit'),
        path('delete/', GenreDeleteView.as_view(), name='genre delete'),
    ])),
    path('device/add/', DeviceAddView.as_view()),
    path('devices/<int:pk>/', include([
        path('details/', DeviceDetailsView.as_view(), name='device details'),
        path('edit/', DeviceEditView.as_view(), name='device edit'),
        path('delete/', DeviceDeleteView.as_view(), name='device delete'),
    ]))
)
