from django.db import models
from bot.models import Bot
from django.contrib.auth import get_user_model


User = get_user_model()


class Reviews(models.Model):
    bot = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        verbose_name='Бот'
    )
    text = models.TextField(
        'Текст отзыва'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор отзыва'
    )
    pub_date = models.DateField(
        'Дата',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date', )

    def __str__(self):
        return f'Отзыв {self.author} на бота {self.bot}'