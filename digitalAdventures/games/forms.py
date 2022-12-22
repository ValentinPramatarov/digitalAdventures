from django import forms
from digitalAdventures.games.models import Game, Genre, Device


# Anyone
class GameAddForm(forms.ModelForm):
    class Meta:
        model = Game
        # fields = ('name', 'image', 'developer', 'developer_site_link', 'release_date', 'synopsis',)
        exclude = ('added_by', )
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }

    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
        # widget=forms.SelectMultiple
    )

    devices = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
        # widget=forms.SelectMultiple
    )


# Creator of Game entry
class GameEditForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('added_by', )


# Creator of Game entry
class GameDeleteForm(forms.ModelForm):
    pass


# All Genres managed by staff
class GenreAddForm(forms.ModelForm):
    pass


class GenreEditForm(forms.ModelForm):
    pass


class GenreDeleteForm(forms.ModelForm):
    pass


# All devices managed by staff
class DeviceAddForm(forms.ModelForm):
    pass


class DeviceEditForm(forms.ModelForm):
    pass


class DeviceDeleteForm(forms.ModelForm):
    pass
