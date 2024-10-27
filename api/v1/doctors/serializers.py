from rest_framework import serializers
from apps.accounts.models import DoctorProfile, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class DoctorSerializer(serializers.ModelSerializer):
    specialty = CategorySerializer()
    class Meta:
        model = DoctorProfile
        fields = [
            'id', 'name', 'specialty', 'experience_years', 'rating',
            'reviews_count', 'consultation_cost', 'description', 'image',
            'education', 'treatment_approach', 'experience', 'skills'
        ]
        