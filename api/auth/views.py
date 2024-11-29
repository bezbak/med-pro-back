from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import generics, status, viewsets, permissions
from rest_framework_simplejwt.exceptions import AuthenticationFailed, TokenError
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.auth.serializers import RegistrationSerializer,LoginSerializer
from apps.accounts.models import CustomUser, PatientProfile


class RegistrationView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer

    @swagger_auto_schema(
        operation_description='Регистрация нового пользователя',
        operation_summary='Регистрация пользователя',
        operation_id='user_registration',
        tags=['Authentication'],
        responses={
            201: openapi.Response(description="Created - Пользователь успешно зарегистрирован"),
            400: openapi.Response(description="Bad Request - Неверные данные для регистрации"),
        },
    )
    # @action(detail=False, methods=['POST'])
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                validated_data = serializer.validated_data
                validated_data.pop('password2')
                user = CustomUser(**validated_data)
                user.set_password(validated_data['password'])
                user.save()
                if validated_data.get('is_doctor'):
                    pass
                else:
                    PatientProfile.objects.create(user = user)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            except Exception as ex:
                return Response(
                    data={"error": f"User creation failed: {str(ex)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer 
    @swagger_auto_schema(
        operation_description='Авторизация пользователя для получения токена',
        operation_summary='Авторизация пользователя для получения токена',
        operation_id='login_user',
        tags=['Authentication'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email пользователя'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль пользователя'),
            },
        ),
        responses={
            200: openapi.Response(description="OK - Авторизация пользователя прошла успешно."),
            400: openapi.Response(description="Bad Request - Неверный запрос."),
            404: openapi.Response(description="Not Found - Пользователь не найден"),
        },
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response(
                'User does not exist',
                status=status.HTTP_404_NOT_FOUND
            )

        if not user.check_password(password):
            return Response(
                'Incorrect password',
                status=status.HTTP_400_BAD_REQUEST
            )

        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)
        user_id = PatientProfile.objects.get(user=user).pk
        return Response(
            data={
                "access_token": str(access_token),
                "refresh_token": str(refresh_token),
                "user_id": user_id
            },
            status=status.HTTP_200_OK
        )


class LogoutView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        operation_description='Выход для удаления токена',
        operation_summary='Выход для удаления токена',
        operation_id='logout_user',
        tags=['Authentication'],
        responses={
            200: openapi.Response(description="OK - Выход пользователя прошел успешно."),
            400: openapi.Response(description="Bad Request - Неверный запрос."),
        },
    )
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")

            if not refresh_token:
                return Response(
                    'Empty Refresh Token',
                    status=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                'Logged out',
                status=status.HTTP_200_OK
            )

        except TokenError:
            return Response(
                'Invalid token',
                status=status.HTTP_400_BAD_REQUEST
            )