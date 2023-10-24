from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """Конфигурация приложения Reviews."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
    verbose_name = 'Отзыв'
    verbose_name_plural = 'Отзывы'
