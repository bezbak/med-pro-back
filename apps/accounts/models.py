from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin

from django.utils import timezone

from .manager import UserManager
from .validation import PhoneNumberValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number_validator = PhoneNumberValidator()

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
        unique=True,
        blank=True,
        null=True,
        max_length=13,
        help_text=_("Обязательное поле. Должно содержать от 10 цифр (0700 123 456) до 12 цифр (996 700 123 456"),
        validators=[phone_number_validator],
        error_messages={
            "unique": _("Пользователь с таким номером телефона уже существует."),
        },
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
                fields=["phone_number"],
                name="unique_inn_phone",
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
    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    medical_history = models.TextField(verbose_name=_('medical history'), blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()}'s Patient Profile"
    
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
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=255)
    name = models.CharField(max_length=255, verbose_name="Имя")
    specialty = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='doctors', verbose_name="Специализация")
    experience_years = models.PositiveIntegerField(verbose_name="Опыт (лет)")
    rating = models.FloatField(verbose_name="Рейтинг")
    reviews_count = models.PositiveIntegerField(verbose_name="Количество отзывов")
    consultation_cost = models.CharField(max_length=50, verbose_name="Стоимость консультации")
    description = models.TextField(verbose_name="Описание врача")
    image = models.ImageField(upload_to='doctors/', verbose_name="Фото врача")
    education = models.TextField(verbose_name="Образование и квалификации")
    treatment_approach = models.TextField(verbose_name="Подход к лечению")
    experience = models.TextField(verbose_name="Опыт работы")
    skills = models.TextField(verbose_name="Навыки и опыт")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Докторы'
