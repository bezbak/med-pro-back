from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.accounts.views import CustomUserViewSet
from api.v1.doctors.views import CategoryListAPIView, DoctorAPIView, ReviewsAPIView
from api.v1.consultations.views import ConsultationViewSet
from api.auth.views import (
    RegistrationView,
    AuthenticationView
)


router = DefaultRouter(trailing_slash=False)


# router.register(r'register', RegistrationView, basename='register'),
router.register(r'authentication', AuthenticationView, basename='authentication')
router.register(r'profile', CustomUserViewSet, basename='profile')
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'consultations', ConsultationViewSet, basename='consultations')
router.register(r'doctors', DoctorAPIView, basename='doctors')
router.register(r'reviews/', ReviewsAPIView, basename='reviews')

urlpatterns = [
        path("register/", RegistrationView.as_view(), name="register"),
        path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    ]

urlpatterns += router.urls
