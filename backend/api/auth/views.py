from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import generics, status, viewsets, permissions
from rest_framework_simplejwt.exceptions import AuthenticationFailed, TokenError
from rest_framework.response import Response

from api.auth.serializers import RegistrationSerializer
from apps.accounts.models import CustomUser


class RegistrationView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                validated_data = serializer.validated_data
                validated_data.pop('password2')
                user = CustomUser(**validated_data)
                user.set_password(validated_data['password'])
                user.save()

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


class AuthenticationView(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def login(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = CustomUser.objects.get(email=email)

        except CustomUser.DoesNotExist:
            return Response(
                'User does not exist',
                status=status.HTTP_404_NOT_FOUND
            )

        if user is None:
            raise AuthenticationFailed('User does not exist')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)

        return Response(
            data={
                "access_token": str(access_token),
                "refresh_token": str(refresh_token)
            },
            status=status.HTTP_200_OK
        )
