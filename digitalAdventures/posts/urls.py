from django.urls import path

from digitalAdventures.posts.views import ImagePostDetailsView, ImagePostCreateView, ImagePostEditView, \
    ImagePostDeleteView

urlpatterns = (
    path('add/', ImagePostCreateView.as_view(), name='post create'),
    path('<int:pk>/details/', ImagePostDetailsView.as_view(), name='post details'),
    path('<int:pk>/edit/', ImagePostEditView.as_view(), name='post edit'),
    path('<int:pk>/delete/', ImagePostDeleteView.as_view(), name='post delete')
)
