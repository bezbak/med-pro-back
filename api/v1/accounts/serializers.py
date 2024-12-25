from rest_framework import serializers

from apps.accounts.models import (
    CustomUser,
    PatientProfile,
    DoctorProfile,
    Reviews
)
from api.v1.consultations.serializers import ConsultationSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_doctor',
            'profile',
            'date_joined'
        ]

class PatientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    consultations = ConsultationSerializer(many=True)
    class Meta:
        model = PatientProfile
        fields = ['medical_history', 'user', 'consultations']


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = [
            'specialization',
            'experience',
            'rating'
        ]