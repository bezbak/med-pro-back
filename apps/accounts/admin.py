from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm
)
from django.utils.translation import gettext_lazy as _

# from .forms import 
from .models import CustomUser, DoctorProfile,Category, PatientProfile, Reviews

admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
# @admin.register(DoctorProfile)
# class DoctorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'specialty', 'experience_years', 'rating')
#     search_fields = ('name', 'specialty')
    

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        ('Пользователь', {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    'profile',
                    "phone_number",
                )
            }
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_doctor",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    'profile',
                    "phone_number",
                ),
            },
        ),
    )

    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ("email", "is_superuser", "is_staff", "is_doctor")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
