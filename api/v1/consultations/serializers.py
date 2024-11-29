from rest_framework import serializers
from apps.consultations.models import Consultation
from api.v1.doctors.serializers import DoctorSerializer

class ConsultationSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=False)
    class Meta:
        model = Consultation
        fields = '__all__'
