from django.db import models
from django.contrib.auth.models import AbstractUser


class ProUser(AbstractUser):
    class Role(models.TextChoices):
        COACH = "t", "Тренер"
        OWNER = "o", "Владелец"
        USER = "u", "Обычный пользователь"
        ARBITER = "a", "Арбитер"
        __empty__ = "Выберите ваш статус:"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    role = models.CharField(max_length=1, choices=Role.choices, default=Role.USER, null=True)
    tickets = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"
        db_table = "db_authorization_user"
        unique_together = ("first_name", "last_name")
