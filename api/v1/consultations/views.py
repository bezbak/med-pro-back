from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.consultations.models import Consultation
from .serializers import ConsultationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from collections import defaultdict

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(patient=self.request.user.patient_profile)

class DoctorScheduleAPIView(APIView):
    def get(self, request, doctor_id):
        # Фильтруем консультации для указанного доктора, у которых есть дата и время
        consultations = Consultation.objects.filter(
            doctor_id=doctor_id,
            date__isnull=False,
            time__isnull=False
        ).values('date', 'time')

        # Группируем слоты по датам
        schedule = defaultdict(lambda: {"busy_slots": []})
        for consultation in consultations:
            date = consultation['date'].isoformat()  # Преобразуем дату в строку
            time = consultation['time'].strftime('%H:%M')  # Форматируем время
            schedule[date]["busy_slots"].append(time)

        # Преобразуем результат в словарь
        schedule_dict = dict(schedule)

        # Возвращаем данные в виде JSON
        return Response(schedule_dict)