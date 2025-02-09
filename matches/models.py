from django.db import models
from django.core.exceptions import ValidationError
from clubs.models import Clubs
from authorization.models import ProUser


class Matches(models.Model):
    First_club = models.ForeignKey(
        Clubs,
        on_delete=models.CASCADE,
        verbose_name="Первый клуб",
        related_name="first_club_matches",
    )
    Second_club = models.ForeignKey(
        Clubs,
        on_delete=models.CASCADE,
        verbose_name="Второй клуб",
        related_name="second_club_matches",
    )
    Date = models.DateTimeField(verbose_name="Дата и время матча")
    Arbiter = models.ForeignKey(
        ProUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Арбитер матча",
        related_name="arbiter_matches",
        limit_choices_to={"role": "a"},
    )
    City = models.CharField(max_length=30, verbose_name="Место проведения")

    def clean(self):
        if self.First_club == self.Second_club:
            raise ValidationError("Первый и второй клуб не могут быть одинаковыми.")

        match_date = self.Date.date()

        if (
            Matches.objects.filter(
                models.Q(First_club=self.First_club)
                | models.Q(Second_club=self.First_club),
                Date__date=match_date,
            )
            .exclude(pk=self.pk)
            .exists()
        ):
            raise ValidationError(
                f"{self.First_club} уже задействован в другом матче в этот день."
            )

        if (
            Matches.objects.filter(
                models.Q(First_club=self.Second_club)
                | models.Q(Second_club=self.Second_club),
                Date__date=match_date,
            )
            .exclude(pk=self.pk)
            .exists()
        ):
            raise ValidationError(
                f"{self.Second_club} уже задействован в другом матче в этот день."
            )

        if (
            Matches.objects.filter(Arbiter=self.Arbiter, Date__date=match_date)
            .exclude(pk=self.pk)
            .exists()
        ):
            raise ValidationError(
                f"Арбитер {self.Arbiter} уже задействован в другом матче в этот день."
            )

    def __str__(self):
        return f"{self.First_club} и {self.Second_club}"

    class Meta:
        verbose_name_plural = "Матчи"
        verbose_name = "Матч"
        db_table = "db_matches"
