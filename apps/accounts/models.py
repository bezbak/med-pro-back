from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from .manager import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    profile = models.ImageField(
        upload_to="profile/",
        null=True,
        blank=True,
        verbose_name=_("Profile")
    )
    phone_number = models.CharField(
        verbose_name=_("Номер телефона"),
        blank=True,
        null=True,
        max_length=13,
    )
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_doctor = models.BooleanField(_('doctor'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("date_joined",)
        verbose_name = _("user")
        verbose_name_plural = _("users")
        app_label = "accounts"

        constraints = [
            models.UniqueConstraint(
                fields=["email"],
                name="unique_inn_email",
            )
        ]

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class PatientProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    medical_history = models.TextField(verbose_name=_('medical history'), blank=True, null=True)

    def __str__(self):
        return f"{self.pk} {self.user.get_full_name()}'s Patient Profile"
    
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        

class Category(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=255)
    image = models.ImageField(verbose_name='Фото услуги', upload_to='category/')
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
    
class DoctorProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    specialty = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='doctors', verbose_name="Специализация")
    experience_years = models.PositiveIntegerField(verbose_name="Опыт (лет)")
    rating = models.FloatField(verbose_name="Рейтинг",validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    reviews_count = models.PositiveIntegerField(verbose_name="Количество отзывов")
    consultation_cost = models.CharField(max_length=50, verbose_name="Стоимость консультации")
    description = models.TextField(verbose_name="Описание врача")
    education = models.TextField(verbose_name="Образование и квалификации")
    treatment_approach = models.TextField(verbose_name="Подход к лечению")
    experience = models.TextField(verbose_name="Опыт работы")
    skills = models.TextField(verbose_name="Навыки и опыт")
    
    def __str__(self):
        return f"{self.user.get_full_name()}'s Doctor Profile"

    
    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Докторы'

class Reviews(models.Model):
    text = models.TextField(
        verbose_name='Текст отзыва'
    )
    doctor = models.ForeignKey(
        DoctorProfile,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Профиль доктора'
    )
    patient = models.ForeignKey(
        PatientProfile,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Пациент'
    )
    stars = models.SmallIntegerField(
        verbose_name='Колличество звёзд',
        max_length=1
    )
    
    def __str__(self):
        return f"{self.patient.user.first_name} - {self.doctor.user.first_name}"
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'