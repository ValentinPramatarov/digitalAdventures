from django import forms

from digitalAdventures.games.models import Game
from digitalAdventures.posts.models import ImagePost


class ImagePostCreateForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ('private', 'photo', 'description', 'game')

        widgets = {
            'private': forms.CheckboxInput(),
        }

    game = forms.ModelChoiceField(queryset=Game.objects.all())


class ImagePostEditForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ('private', 'description', 'game')

        widgets = {
            'private': forms.CheckboxInput(),
        }

    game = forms.ModelChoiceField(queryset=Game.objects.all())
