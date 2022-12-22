from django import forms
from digitalAdventures.games.models import Game, Genre, Device


class GameAddForm(forms.ModelForm):
    class Meta:
        model = Game
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


class GameEditForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'image', 'developer', 'developer_site_link', 'release_date', 'synopsis',)

        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'synopsis': forms.Textarea()
        }

    devices = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class GenreAddForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', 'description')


class GenreEditForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', 'description', )

        widgets = {
            'description': forms.Textarea()
        }


class DeviceAddForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('name', 'maker', 'image', 'release_date')

        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }


class DeviceEditForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('name', 'maker', 'image', 'release_date', )

        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }


