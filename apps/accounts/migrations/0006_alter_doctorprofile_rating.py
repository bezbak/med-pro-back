# Generated by Django 5.0.7 on 2024-11-16 12:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Рейтинг'),
        ),
    ]
