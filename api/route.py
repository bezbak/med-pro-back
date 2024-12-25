from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.accounts.views import CustomUserViewSet, PatientViewSet
from api.v1.doctors.views import CategoryListAPIView, DoctorAPIView, ReviewsAPIView,FavoritesAPIView
from api.v1.consultations.views import ConsultationViewSet,DoctorScheduleAPIView
from api.auth.views import (
    RegistrationView,
    LoginView,
    LogoutView
)


router = DefaultRouter(trailing_slash=False)


# router.register(r'register', RegistrationView, basename='register'),
# router.register(r'authentication', AuthenticationView, basename='authentication')
router.register(r'profile', CustomUserViewSet, basename='profile')
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'consultations', ConsultationViewSet, basename='consultations')
router.register(r'doctors', DoctorAPIView, basename='doctors')
router.register(r'reviews/', ReviewsAPIView, basename='reviews')
router.register(r'favorites/', FavoritesAPIView, basename='favorites')
router.register(r'patients', PatientViewSet, basename='patients')

urlpatterns = [
        path("register/", RegistrationView.as_view(), name="register"),
        path("login/", LoginView.as_view(), name="login"),
        path("logout/", LogoutView.as_view(), name="logout"),
        path('categories/', CategoryListAPIView.as_view(), name='category_list'),
        path('shedule/<int:doctor_id>/', DoctorScheduleAPIView.as_view(), name='shedule_list'),
    ]

urlpatterns += router.urls
