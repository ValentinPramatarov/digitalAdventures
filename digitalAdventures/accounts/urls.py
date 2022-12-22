from django.urls import path

from django.contrib.auth.decorators import login_required
from digitalAdventures.accounts.views import SignUpView, UserDetailsView, UserEditView, SignInView, SignOutView, \
    UserDeleteView

urlpatterns = (
    path('create/', SignUpView.as_view(), name='user sign up'),
    path('login/', SignInView.as_view(), name='user sign in'),
    path('logout/', SignOutView.as_view(), name='user sign out'),
    path('<int:pk>/details/', login_required(UserDetailsView.as_view()), name='user details'),
    path('<int:pk>/edit/', login_required(UserEditView.as_view()), name='user edit'),
    path('<int:pk>/delete/', login_required(UserDeleteView.as_view()), name='user delete')
    # path('<int:pk>/add-profile-picture/', add_profile_picture, name='user upload profile picture')
)
