from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.accounts.models import CustomUser, DoctorProfile, PatientProfile
from .serializers import (
    UserSerializer,
    PatientProfileSerializer,
    DoctorProfileSerializer
)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.AllowAny,)    # todo: change for permission
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Список пользователей.",
        operation_summary="Список пользователей.",
        operation_id="list_users",
        tags=["Пользователь(User)"],
        responses={
            200: openapi.Response(description="OK - Список пользователей получен успешно."),
            401: openapi.Response(description="Ошибка аутентификации"),
        },
    )
    @action(detail=True, methods=['GET'], url_path='list')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получить профиль.",
        operation_summary="Получить профиль.",
        operation_id="detail_user",
        tags=["Пользователь(User)"],
        responses={
            200: openapi.Response(description="OK - Профиль пользователя получено успешно."),
            401: openapi.Response(description="Ошибка аутентификации"),
            404: openapi.Response(description="Not Found - Пользователь не найден"),
        },
    )
    @action(detail=False, methods=['GET'], url_path='user-profile')
    def user_profile(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_serializer = UserSerializer(request.user)
            user_data = user_serializer.data

            if request.user.is_doctor:
                try:
                    dr_profile = DoctorProfile.objects.get(user=request.user)
                    dr_serializer = DoctorProfileSerializer(dr_profile)
                    user_data['doctor_profile'] = dr_serializer.data
                except DoctorProfile.DoesNotExist:
                    user_data['doctor_profile'] = None
            else:
                try:
                    pt_profile = PatientProfile.objects.get(user=request.user)
                    pt_serializer = PatientProfileSerializer(pt_profile)
                    user_data['patient_profile'] = pt_serializer.data
                except PatientProfile.DoesNotExist:
                    user_data['patient_profile'] = None
            return Response(
                data=user_data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'detail': 'You are not logged in.'},
                status=status.HTTP_403_FORBIDDEN
            )