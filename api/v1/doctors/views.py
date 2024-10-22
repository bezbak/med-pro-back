from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from .serializers import DoctorSerializer
from apps.accounts.models import DoctorProfile

class DoctorListAPIView(APIView):
    def get(self, request):
        doctors = DoctorProfile.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoctorDetailAPIView(APIView):
    def get(self, request, doctor_id):
        try:
            doctor = DoctorProfile.objects.get(id=doctor_id)
        except DoctorProfile.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)