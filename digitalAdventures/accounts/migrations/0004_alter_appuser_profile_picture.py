# Generated by Django 4.1.4 on 2022-12-23 07:59

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_appuser_favourite_game_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='user_photos/', validators=[core.validators.validate_file_less_than_5mb]),
        ),
    ]
