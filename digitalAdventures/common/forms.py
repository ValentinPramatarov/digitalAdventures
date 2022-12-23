from django import forms
from digitalAdventures.posts.models import ImageComment


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = ImageComment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add comment...',
                }
            )
        }


class SearchGamesForm(forms.Form):
    game_name = forms.CharField(
        max_length=50,
        required=False,
    )
