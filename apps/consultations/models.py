from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.accounts.models import PatientProfile, DoctorProfile
from .choices import ConsultationStatus


class Consultation(models.Model):
    patient = models.ForeignKey(
        PatientProfile,
        related_name='consultations',
        on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        DoctorProfile,
        related_name='doctor_consultations',
        on_delete=models.CASCADE
    )
    date = models.DateField(verbose_name='Дата записи', blank=True, null=True)
    time = models.TimeField(verbose_name='Время записи', blank=True, null=True)
    consul_type = models.CharField(verbose_name="Тип консультации", max_length=250)
    wh_number = models.CharField(verbose_name="Номер WhatsApp", max_length=15)
    status = models.CharField(
        max_length=10,
        choices=ConsultationStatus.CHOICES,
        default=ConsultationStatus.PENDING,
        verbose_name=_('status')
    )
    notes = models.TextField(verbose_name=_('notes'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    class Meta:
        ordering = ['-date']
        verbose_name = _('consultation')
        verbose_name_plural = _('consultations')

    def __str__(self):
        return (f'Consultation between {self.patient.user.get_full_name()} and \
                Dr. {self.doctor.user.get_full_name()} on {self.date} {self.time}')



