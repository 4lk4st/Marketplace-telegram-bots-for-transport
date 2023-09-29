from bot.models import Bot
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Shopping_cart(models.Model):
    """Боты в корзине покупок."""
    bot = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        related_name='in_shopping_cart',
        verbose_name='Боты в корзине покупок',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='in_shopping_cart',
        verbose_name='Владелец корзины покупок',
    )

    class Meta:
        verbose_name = 'Бот в корзине покупок'
        verbose_name_plural = 'Боты в корзине покупок'
        constraints = [
            models.UniqueConstraint(
                fields=(
                    'user',
                    'bot'
                ),
                name='unique_in_shopping_cart'
            )
        ]

    def __str__(self):
        return f'{self.bot} - {self.user}'
