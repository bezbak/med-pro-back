from django.contrib import admin
from .models import Consultation


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date_time', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'date_time']
    search_fields = ['patient__user__first_name', 'patient__user__last_name', 'doctor__user__first_name', 'doctor__user__last_name']
