from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

# Create your views here.
from .serializers import DoctorSerializer, CategorySerializer
from apps.accounts.models import DoctorProfile, Category

class DoctorAPIView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['name', 'description']
    filterset_fields = ('specialty',)
    
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer