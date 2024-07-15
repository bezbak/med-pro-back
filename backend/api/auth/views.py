from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import generics, status, viewsets, permissions

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
