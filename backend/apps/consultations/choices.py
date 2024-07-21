from django.utils.translation import gettext_lazy as _


class ConsultationStatus:
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

    CHOICES = [
        (PENDING, _('Pending')),
        (CONFIRMED, _('Confirmed')),
        (COMPLETED, _('Completed')),
        (CANCELLED, _('Cancelled')),
    ]