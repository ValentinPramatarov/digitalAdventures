from django.db import models


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

    image = models.URLField(
        null=False,
        blank=False,
        verbose_name="Game image link"
    )

    developer = models.CharField(
        max_length=DEVELOPER_NAME_MAX_LEN,
        null=False,
        blank=False,
        verbose_name="Developer name"
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
        verbose_name="Genre name"
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        blank=False,
        null=False,
    )

    games = models.ManyToManyField(Game)

    def __str__(self):
        return self.name


class Device(models.Model):
    DEVICE_NAME_MAX_LEN = 20
    DEVICE_MAKER_MAX_LEN = 30

    name = models.CharField(
        max_length=DEVICE_NAME_MAX_LEN,
        blank=False,
        null=False,
        verbose_name='Device name'
    )

    maker = models.CharField(
        max_length=DEVICE_MAKER_MAX_LEN,
        blank=False,
        null=False,
        verbose_name='Device maker'
    )

    image = models.URLField(
        null=False,
        blank=False,
        verbose_name="Device image link"
    )

    release_date = models.DateField(
        null=False,
        blank=False,
    )

    games = models.ManyToManyField(Game)

    def __str__(self):
        return self.name
