from django.urls import path

from digitalAdventures.accounts.views import SignUpView, UserDetailsView, UserEditView

urlpatterns = (
    path('create/', SignUpView.as_view(), name='user sign up'),
    path('<int:pk>/edit/', UserEditView.as_view(), name='user edit'),
)
