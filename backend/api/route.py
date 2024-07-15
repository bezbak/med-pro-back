from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.accounts.views import CustomUserViewSet
from api.auth.views import RegistrationView

router = DefaultRouter(trailing_slash=False)
urlpatterns = router.urls


urlpatterns.extend(
    [
# User
        path("users/", CustomUserViewSet.as_view({"get": "list"})),
        path("users/profile/", CustomUserViewSet.as_view({"get": "user_profile"})),
        # path(
        #     "users/<slug:slug>/",
        #     CustomUserViewSet.as_view(
        #         {
        #             "get": "user_detail",
        #             "put": "update_detail",
        #         }
        #     ),
        # ),
# Registration
        path("register/", RegistrationView.as_view(), name="register"),


    ]
)