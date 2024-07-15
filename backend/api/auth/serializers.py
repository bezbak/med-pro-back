from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from apps.accounts.models import CustomUser, PatientProfile, DoctorProfile


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        # validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'phone_number',
            'password',
            'password2',
            'last_name',
            'is_doctor',
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {
                    "password": "Password fields didn't match."
                }
            )
        return attrs


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
