# Generated by Django 4.1.2 on 2022-10-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("war", "0002_game_initial_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="initial_status",
            field=models.JSONField(default=dict),
        ),
    ]