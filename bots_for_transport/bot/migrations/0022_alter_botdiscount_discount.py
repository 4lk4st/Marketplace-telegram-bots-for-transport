# Generated by Django 4.2.4 on 2023-11-01 14:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0021_alter_botdiscount_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botdiscount',
            name='discount',
            field=models.DecimalField(decimal_places=0, default=0, help_text='Введите скидку от автора в процентах (от 0 до 100).', max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка'),
        ),
    ]