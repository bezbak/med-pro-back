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


class PatientProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    medical_history = models.TextField(verbose_name=_('medical history'), blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()}'s Patient Profile"


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    specialization = models.CharField(max_length=255, verbose_name=_('specialization'),)
    experience = models.IntegerField(verbose_name=_('experience'))
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.0,
        verbose_name=_('rating')
    )

    def __str__(self):
        return f"Dr. {self.user.get_full_name()}'s Profile"
