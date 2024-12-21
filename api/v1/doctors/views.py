from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet  
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from .serializers import DoctorSerializer, CategorySerializer, ReviewsSerializer
from apps.accounts.models import DoctorProfile, Category, Reviews

class DoctorAPIView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['user__first_name','user__last_name', 'description', 'specialty__name']
    filterset_fields = ('specialty',)
    
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ReviewsAPIView(GenericViewSet,ListModelMixin, CreateModelMixin):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ('doctor','patient')
    