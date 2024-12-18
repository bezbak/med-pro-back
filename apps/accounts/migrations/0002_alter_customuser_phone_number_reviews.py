# Generated by Django 5.0.7 on 2024-11-08 11:57

import apps.accounts.validation
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Обязательное поле. Должно содержать от 10 цифр (0700 123 456) до 12 цифр (996 700 123 456', max_length=13, null=True, unique=True, validators=[apps.accounts.validation.PhoneNumberValidator()], verbose_name='Номер телефона'),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('stars', models.SmallIntegerField(max_length=2, verbose_name='Колличество звёзд')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='accounts.doctorprofile', verbose_name='Профиль доктора')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='accounts.patientprofile', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
