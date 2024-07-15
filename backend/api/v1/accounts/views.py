from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions

from apps.accounts.models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)    # todo: change for permission

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def user_profile(self, request, *args, **kwargs):
        try:
            serializer = CustomUserSerializer(request.user)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
