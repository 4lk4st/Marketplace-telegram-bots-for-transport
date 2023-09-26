from django.apps import AppConfig


class FavoriteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'favorite'
    verbose_name = 'Избранный'
    verbose_name_plural = 'Избранные'