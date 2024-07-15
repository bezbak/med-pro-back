from rest_framework import serializers

from apps.accounts.models import (
    CustomUser,
    PatientProfile,
    DoctorProfile
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_doctor',
            'date_joined'
        ]


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['medical_history']


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = [
            'specialization',
            'experience',
            'rating'
        ]
