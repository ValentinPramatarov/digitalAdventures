from django.db import models
from core.validators import validate_file_less_than_5mb
import digitalAdventures.settings

# UserModel is defined this way to escape circular import
UserModel = digitalAdventures.settings.AUTH_USER_MODEL


class Game(models.Model):
    GAME_NAME_MAX_LEN = 45
    DEVELOPER_NAME_MAX_LEN = 30
    SYNOPSIS_MAX_LEN = 150

    name = models.CharField(
        max_length=GAME_NAME_MAX_LEN,
        blank=False,
        null=False,
        verbose_name="Game name"
    )

    image = models.ImageField(
        upload_to='games/',
        null=False,
        blank=False,
        validators=(validate_file_less_than_5mb, ),
        verbose_name="Game image"
    )

    developer = models.CharField(
        max_length=DEVELOPER_NAME_MAX_LEN,
        null=False,
        blank=False,
        verbose_name="Developer name"
    )

    developer_site_link = models.URLField(
        null=True,
        blank=True,
    )

    release_date = models.DateField(
        null=False,
        blank=False,
    )

    synopsis = models.TextField(
        max_length=SYNOPSIS_MAX_LEN,
        null=True,
        blank=True,
    )

    added_by = models.ForeignKey(
        UserModel, on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    # TODO: Think of picture/banner implementation
    GENRE_NAME_MAX_LEN = 45
    DESCRIPTION_MAX_LEN = 150

    name = models.CharField(
        max_length=GENRE_NAME_MAX_LEN,
        blank=False,
        null=False,
        unique=True,
        verbose_name="Genre name"
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        blank=False,
        null=False,
        unique=True,
    )

    games = models.ManyToManyField(Game, related_name='genres')

    def __str__(self):
        return self.name


class Device(models.Model):
    DEVICE_NAME_MAX_LEN = 20
    DEVICE_MAKER_MAX_LEN = 30

    name = models.CharField(
        max_length=DEVICE_NAME_MAX_LEN,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Device name'
    )

    maker = models.CharField(
        max_length=DEVICE_MAKER_MAX_LEN,
        blank=False,
        null=False,
        verbose_name='Device maker'
    )

    image = models.ImageField(
        upload_to='consoles/',
        null=False,
        blank=False,
        validators=(validate_file_less_than_5mb, )
    )

    release_date = models.DateField(
        null=False,
        blank=False,
    )

    games = models.ManyToManyField(Game, related_name='devices')

    def __str__(self):
        return self.name
