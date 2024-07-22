from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.accounts.views import CustomUserViewSet
from api.auth.views import RegistrationView, AuthenticationView

router = DefaultRouter(trailing_slash=False)


# router.register(r'register', RegistrationView, basename='register'),
router.register(r'authentication', AuthenticationView, basename='authentication')
router.register(r'profile', CustomUserViewSet, basename='profile')

urlpatterns = [
# Authentication/Authorization
        path("register/", RegistrationView.as_view(), name="register"),
        # path("login/", AuthenticationView.as_view({'post': 'login'}), name="login"),
        # path("logout/", AuthenticationView.as_view({"post": "logout"}), name="logout"),
# # User
#         path("users/", CustomUserViewSet.as_view({"get": "list"})),
#         path("users/profile/", CustomUserViewSet.as_view({"get": "user_profile"})),
    ]

urlpatterns += router.urls
