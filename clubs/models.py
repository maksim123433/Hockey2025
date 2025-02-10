from django.db import models
from django.core.exceptions import ValidationError


from authorization.models import ProUser


class Clubs(models.Model):

    class ConferenceChoices(models.TextChoices):
        EASTERN = "e", "Восточная"
        WESTERN = "w", "Западная"
        __empty__ = "Выберите конференцию"

    Name = models.CharField(
        max_length=100, verbose_name="Название клуба", unique=True, null=False
    )
    Foundation_date = models.DateField(verbose_name="Дата основания", null=False)
    Head_coach = models.OneToOneField(
        ProUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": "t"},
        verbose_name="Главный тренер",
        unique=True,
        related_name="coached_clubs",
    )
    Number_of_players = models.IntegerField(
        verbose_name="Количество игроков", null=False
    )
    Owner = models.ForeignKey(
        ProUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": "o"},
        verbose_name="Владелец",
        related_name="owned_clubs",
    )
    Conference = models.CharField(
        max_length=1,
        choices=ConferenceChoices.choices,
        verbose_name="Конференция",
        null=False,
    )
    Registration_date = models.DateField(
        auto_now_add=True, verbose_name="Дата регистрации", null=False
    )
    Total_cost_of_club = models.FloatField(
        verbose_name="Общая стоимость клуба", null=True
    )

    def clean(self):
        if (
            self.Head_coach
            and Clubs.objects.filter(Head_coach=self.Head_coach)
            .exclude(pk=self.pk)
            .exists()
        ):
            raise ValidationError(
                f"Тренер {self.Head_coach} уже связан с другим клубом."
            )


    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = "Клубы"
        verbose_name = "Клуб"
        db_table = "db_clubs"

# .exclude(pk=self.pk): Этот метод исключает текущий клуб из результатов фильтрации,
# используя его первичный ключ (pk). Это нужно для того, чтобы не учитывать сам текущий
# клуб при проверке на совпадение тренера.
#
# .exists(): Этот метод проверяет, существуют ли объекты,
# удовлетворяющие условиям фильтрации и исключения.
# Возвращает True, если такие объекты существуют, и False, если нет.