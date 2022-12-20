from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy

from digitalAdventures.accounts.forms import UserCreateForm, UserEditForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/user-create-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    pass


class UserEditView(views.UpdateView):
    template_name = 'accounts/user-edit-page.html'
    form_class = UserEditForm
    model = UserModel
    success_url = reverse_lazy('index')
