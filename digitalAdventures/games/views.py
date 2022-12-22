from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin

from digitalAdventures.games.forms import GameAddForm, GameEditForm
from digitalAdventures.games.models import Game, Genre, Device


# class AddGameView(LoginRequiredMixin, views.CreateView):
#     template_name = 'games/game-add-page.html'
#     form_class = GameAddForm
#
#     def form_valid(self, form):
#         form.instance.added_by = self.request.user
#         return super().form_valid(form)

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
        context['object_attributes'] = vars(self.object)
        context['devices'] = self.object.device_set.all()
        context['genres'] = self.object.genre_set.all()

        return context


class GameEditView(views.UpdateView):
    model = Game
    form_class = GameEditForm
    template_name = 'games/game-edit-view.html'
    success_url = reverse_lazy('index')


class GameDeleteView(views.DeleteView):
    pass


class GenreAddView(views.CreateView):
    model = Genre


class GenreDetailsView(views.CreateView):
    model = Genre


class GenreEditView(views.UpdateView):
    model = Genre


class GenreDeleteView(views.DeleteView):
    model = Genre


class DeviceAddView(views.CreateView):
    model = Device


class DeviceDetailsView(views.DetailView):
    model = Device


class DeviceEditView(views.UpdateView):
    model = Device


class DeviceDeleteView(views.DeleteView):
    model = Device
