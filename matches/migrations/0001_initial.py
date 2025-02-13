# Generated by Django 5.1.5 on 2025-02-08 19:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clubs", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Matches",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Date", models.DateTimeField(verbose_name="Дата и время матча")),
                (
                    "City",
                    models.CharField(max_length=30, verbose_name="Место проведения"),
                ),
                (
                    "Arbiter",
                    models.ForeignKey(
                        limit_choices_to={"role": "a"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="arbiter_matches",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Арбитер матча",
                    ),
                ),
                (
                    "First_club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="first_club_matches",
                        to="clubs.clubs",
                        verbose_name="Первый клуб",
                    ),
                ),
                (
                    "Second_club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="second_club_matches",
                        to="clubs.clubs",
                        verbose_name="Второй клуб",
                    ),
                ),
            ],
            options={
                "verbose_name": "Матч",
                "verbose_name_plural": "Матчи",
                "db_table": "db_matches",
            },
        ),
    ]
