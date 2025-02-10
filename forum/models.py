from django.db import models

from authorization.models import ProUser

class Comment(models.Model):
    comment = models.TextField(verbose_name="Комментарий")
    user = models.ForeignKey(
        ProUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Пользователь",
        related_name="comment",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        db_table = "db_comments"

    def __str__(self):
        return f"Комментарий от {self.user.username} на {self.created_at}"
