from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.consultations.models import Consultation
from .serializers import ConsultationSerializer


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(patient=self.request.user.patientprofile)
