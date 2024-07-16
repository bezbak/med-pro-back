from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.accounts.views import CustomUserViewSet
from api.auth.views import RegistrationView, AuthenticationView

router = DefaultRouter(trailing_slash=False)
urlpatterns = router.urls


urlpatterns.extend(
    [
# Authentication/Authorization
        path("register/", RegistrationView.as_view(), name="register"),
        path("login/", AuthenticationView.as_view({'post': 'login'}), name="login"),
        path("logout/", AuthenticationView.as_view({"post": "logout"}), name="logout"),
# User
        path("users/", CustomUserViewSet.as_view({"get": "list"})),
        path("users/profile/", CustomUserViewSet.as_view({"get": "user_profile"})),
    ]
)