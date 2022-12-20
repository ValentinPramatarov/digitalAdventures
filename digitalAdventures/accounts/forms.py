from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")
        field_classes = {
            "username": auth_forms.UsernameField,
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'gender', 'profile_picture', 'description', 'favourite_game',
                  'main_device', 'favourite_genre')
