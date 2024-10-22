from rest_framework import serializers
from apps.accounts.models import DoctorProfile

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = [
            'id', 'name', 'specialty', 'experience_years', 'rating',
            'reviews_count', 'consultation_cost', 'description', 'image',
            'education', 'treatment_approach', 'experience', 'skills'
        ]