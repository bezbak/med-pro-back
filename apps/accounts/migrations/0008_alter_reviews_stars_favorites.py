# Generated by Django 5.0.7 on 2024-12-25 10:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_patientprofile_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='stars',
            field=models.SmallIntegerField(max_length=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Колличество звёзд'),
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='accounts.doctorprofile', verbose_name='Профиль доктора')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='accounts.patientprofile', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Избранные',
                'verbose_name_plural': 'Избранные',
            },
        ),
    ]
