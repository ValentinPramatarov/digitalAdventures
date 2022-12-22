from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin

from core.Mixins import GamePermissionCheckMixin, GenreDevicePermissionCheckMixin
from digitalAdventures.games.forms import GameAddForm, GameEditForm, GenreAddForm, GenreEditForm, DeviceAddForm, \
    DeviceEditForm
from digitalAdventures.games.models import Game, Genre, Device


# class AddGameView(LoginRequiredMixin, views.CreateView):
#     template_name = 'games/game-add-page.html'
#     form_class = GameAddForm
#
#     def form_valid(self, form):
#         form.instance.added_by = self.request.user
#         return super().form_valid(form)

@login_required
def create_game(request):
    if request.method == 'GET':
        form = GameAddForm()

    else:
        form = GameAddForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.added_by = request.user
            game.save()
            form.save_m2m()

            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'games/game-add-page.html', context)

    # TODO: Fix form multiple selection rendering, looks ugly atm


class GameDetailsView(views.DetailView):
    model = Game
    template_name = 'games/game-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        has_permissions = False

        if self.request.user.pk == self.object.added_by:
            has_permissions = True
        elif self.request.user.is_staff or self.request.user.is_superuser:
            has_permissions = True

        context['has_permissions'] = has_permissions
        context['devices'] = self.object.devices.all()
        context['genres'] = self.object.genres.all()

        return context


class GameEditView(GamePermissionCheckMixin, views.UpdateView):
    template_name = 'games/game-edit-view.html'
    form_class = GameEditForm
    model = Game
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.devices.set(form.cleaned_data['devices'])
        self.object.genres.set(form.cleaned_data['genres'])
        return redirect(self.get_success_url())


# def game_edit_view(request, pk):
#     obj = Game.objects.filter(pk=pk).get()
#
#     if request.method == "GET":
#         form = GameEditForm(instance=obj)
#     else:
#         form = GameEditForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('game details', pk=pk)
#
#     context = {
#         'form': form,
#         'pk': pk,
#     }
#
#     return render(request, 'games/game-edit-view.html', context)


class GameDeleteView(GamePermissionCheckMixin, views.DeleteView):
    model = Game
    success_url = reverse_lazy('index')
    template_name = 'games/game-delete-page.html'


class GenreAddView(LoginRequiredMixin, GenreDevicePermissionCheckMixin, views.CreateView):
    model = Genre
    form_class = GenreAddForm
    template_name = 'games/genre-add-page.html'
    success_url = reverse_lazy('index')


class GenreDetailsView(views.DetailView):
    model = Genre
    template_name = 'games/genre-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        has_permissions = False

        if self.request.user.is_staff or self.request.user.is_superuser:
            has_permissions = True

        context['has_permissions'] = has_permissions
        context['games'] = self.object.games.all()

        return context


class GenreEditView(LoginRequiredMixin, GenreDevicePermissionCheckMixin, views.UpdateView):
    model = Genre
    template_name = 'games/genre-edit-page.html'
    form_class = GenreEditForm
    success_url = reverse_lazy('index')


class GenreDeleteView(LoginRequiredMixin, GenreDevicePermissionCheckMixin, views.DeleteView):
    model = Genre
    success_url = reverse_lazy('index')
    template_name = 'games/genre-delete-page.html'


class DeviceAddView(LoginRequiredMixin, GenreDevicePermissionCheckMixin, views.CreateView):
    model = Device
    form_class = DeviceAddForm
    template_name = 'games/device-add-page.html'
    success_url = reverse_lazy('index')

    # TODO: Fix release_date, currently not displaying as widget


class DeviceDetailsView(views.DetailView):
    model = Device
    template_name = 'games/device-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        has_permissions = False

        if self.request.user.is_staff or self.request.user.is_superuser:
            has_permissions = True

        context['has_permissions'] = has_permissions
        context['games'] = self.object.games.all()

        return context


class DeviceEditView(LoginRequiredMixin, GenreDevicePermissionCheckMixin, views.UpdateView):
    model = Device
    template_name = 'games/device-edit-page.html'
    form_class = DeviceEditForm
    success_url = reverse_lazy('index')


class DeviceDeleteView(LoginRequiredMixin, GenreDevicePermissionCheckMixin, views.DeleteView):
    model = Device
    success_url = reverse_lazy('index')
    template_name = 'games/device-delete-page.html'
