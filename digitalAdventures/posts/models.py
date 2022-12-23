from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator
from core.validators import validate_file_less_than_5mb
from digitalAdventures.games.models import Game

UserModel = get_user_model()


class ImagePost(models.Model):

    MAX_DESCRIPTION_LENGTH = 100

    private = models.BooleanField(
        null=False,
        blank=False,
    )

    photo = models.ImageField(
        upload_to='adventure_photos/',
        null=False,
        blank=False,
        validators=(validate_file_less_than_5mb, ),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=False,
    )

    likes = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=False,
    )

    liked_by = models.ManyToManyField(
        UserModel,
        related_name='liked_by'
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='image_posts'
    )

    posted_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='posts'
    )


class ImageComment(models.Model):
    MIN_COMMENT_LENGTH = 10
    MAX_COMMENT_LENGTH = 200

    content = models.CharField(
        max_length=MAX_COMMENT_LENGTH,
        validators=(
            MinLengthValidator(MIN_COMMENT_LENGTH),
        ),
        null=False,
        blank=False,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=False,
    )

    posted_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='image_comments'
    )

    related_post = models.ForeignKey(
        ImagePost,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='comments'
    )
