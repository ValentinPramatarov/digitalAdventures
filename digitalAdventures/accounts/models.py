from django.db import models
from django.contrib.auth import models as auth_models
from django.core import validators

from core.utils import double_collection_max_str_len
from core.validators import validate_only_letters, validate_file_less_than_5mb
from digitalAdventures.games.models import Game, Device, Genre


class AppUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 20

    DESCRIPTION_MAX_LEN = 150

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=double_collection_max_str_len(GENDER_CHOICES),
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to='user_photos/',
        blank=True,
        null=True,
        validators=(validate_file_less_than_5mb, )
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        blank=True,
        null=True,
    )

    favourite_game = models.ForeignKey(
        Game,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    main_device = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    favourite_genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
