from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.accounts.views import CustomUserViewSet
from api.v1.doctors.views import DoctorDetailAPIView, DoctorListAPIView
from api.v1.consultations.views import ConsultationViewSet
from api.auth.views import (
    RegistrationView,
    AuthenticationView
)


router = DefaultRouter(trailing_slash=False)


# router.register(r'register', RegistrationView, basename='register'),
router.register(r'authentication/', AuthenticationView, basename='authentication')
router.register(r'profile/', CustomUserViewSet, basename='profile')
router.register(r'users/', CustomUserViewSet, basename='users')
router.register(r'consultations/', ConsultationViewSet, basename='consultations')


urlpatterns = [
        path("register/", RegistrationView.as_view(), name="register"),
        path('doctors/', DoctorListAPIView.as_view(), name='doctor_list'),
        path('doctors/<int:doctor_id>/', DoctorDetailAPIView.as_view(), name='doctor_detail'),
    ]

urlpatterns += router.urls
