from django.urls import path

from digitalAdventures.common.views import index, like_post, comment_post

urlpatterns = (
    path('', index, name='index'),
    path('<int:pk>/like/', like_post, name='like post'),
    path('<int:pk>/comment/', comment_post, name='comment post'),

)
