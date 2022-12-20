from django.urls import path

from digitalAdventures.accounts.views import SignUpView

urlpatterns = (
    path('create/', SignUpView.as_view(), name='user sign up'),
)
