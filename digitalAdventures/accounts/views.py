from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import default_storage
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy

from core.Mixins import AccountPermissionCheckMixin
from digitalAdventures.accounts.forms import UserCreateForm, UserEditForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/user-create-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignInView(auth_views.LoginView):
    template_name = 'accounts/user-login-page.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView, LoginRequiredMixin):
    model = UserModel
    template_name = 'accounts/user-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['profile_picture'] = self.object.profile_picture or None
        context['games'] = self.object.game_set.all()

        return context


class UserEditView(AccountPermissionCheckMixin, views.UpdateView):
    template_name = 'accounts/user-edit-page.html'
    form_class = UserEditForm
    model = UserModel
    success_url = reverse_lazy('index')

    # Doesn't render view if logged-in user is not owner of account


class UserDeleteView(AccountPermissionCheckMixin, views.DeleteView):
    model = UserModel
    success_url = reverse_lazy('index')
    template_name = 'accounts/user-delete-page.html'


# def add_profile_picture(request, pk):
#     user = get_object_or_404(UserModel, pk=pk)
#     print(user.username)
#     print(user.favourite_genre)
#     print(user.profile_picture)
#
#     if request.method == "GET":
#         form = UserProfilePictureUploadForm()
#     else:
#         form = UserProfilePictureUploadForm(request.POST, request.FILES)
#         print(request.FILES)
#         if form.is_valid():
#             image = request.FILES['profile_picture']
#             file_path = default_storage.save(f'user_photos/{image.name}', image)
#             user.image = file_path
#             user.save()
#
#             return redirect(reverse_lazy('index'))
#
#     context = {
#         "form": form,
#         "pk": pk,
#     }
#
#     # TODO: Handle case where user already has uploaded a profile picture
#
#     return render(request, "accounts/user-upload-profile-picture.html", context)
