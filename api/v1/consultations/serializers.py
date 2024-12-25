from rest_framework import serializers
from apps.consultations.models import Consultation
from apps.accounts.models import DoctorProfile
from api.v1.doctors.serializers import DoctorSerializer

class ConsultationSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=False, read_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=DoctorProfile.objects.all(),
        source='doctor',
        write_only=True
    )
    class Meta:
        model = Consultation
        fields = '__all__'
