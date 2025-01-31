# Generated by Django 4.2.6 on 2023-11-09 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("bot", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reviews",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор отзыва",
            ),
        ),
        migrations.AddField(
            model_name="reviews",
            name="bot",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review",
                to="bot.bot",
                verbose_name="Бот",
            ),
        ),
    ]
