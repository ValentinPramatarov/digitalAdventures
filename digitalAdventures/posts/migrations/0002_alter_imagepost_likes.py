# Generated by Django 4.1.4 on 2022-12-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
