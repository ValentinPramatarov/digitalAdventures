from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from core.mixins import UnauthenticatedAndPostIsPrivateCheckMixin, \
    PostAccountPermissionCheckMixin
from digitalAdventures.posts.forms import ImagePostCreateForm, ImagePostEditForm
from digitalAdventures.posts.models import ImagePost


class ImagePostCreateView(LoginRequiredMixin, views.CreateView):
    model = ImagePost
    form_class = ImagePostCreateForm
    template_name = 'posts/image-post-create-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class ImagePostDetailsView(UnauthenticatedAndPostIsPrivateCheckMixin, views.DetailView):
    model = ImagePost
    template_name = 'posts/image-post-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        has_permissions = False

        if self.request.user == self.object.posted_by:
            has_permissions = True

        context['has_permissions'] = has_permissions
        context['comments'] = self.object.comments.all()
        context['has_user_liked_photo'] = self.request.user in self.object.liked_by.all()

        return context


class ImagePostEditView(PostAccountPermissionCheckMixin, views.UpdateView):
    model = ImagePost
    template_name = 'posts/image-post-edit-view.html'
    form_class = ImagePostEditForm
    success_url = reverse_lazy('index')


class ImagePostDeleteView(PostAccountPermissionCheckMixin, views.DeleteView):
    model = ImagePost
    template_name = 'posts/image-post-delete-view.html'
    success_url = reverse_lazy('index')
