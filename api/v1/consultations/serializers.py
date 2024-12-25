from rest_framework import serializers
from apps.consultations.models import Consultation
from apps.accounts.models import DoctorProfile, PatientProfile
from api.v1.doctors.serializers import DoctorSerializer, PatientSerializer

class ConsultationSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=False, read_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=DoctorProfile.objects.all(),
        source='doctor',
        write_only=True
    )
    patient = PatientSerializer(many=False, read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=PatientProfile.objects.all(),
        source='doctor',
        write_only=True
    )
    class Meta:
        model = Consultation
        fields = '__all__'
