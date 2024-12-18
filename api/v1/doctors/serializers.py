from rest_framework import serializers
from apps.accounts.models import DoctorProfile, Category, Reviews, PatientProfile, CustomUser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'email', 'first_name', 'last_name', 'profile',
            'phone_number'
        ]
        
class DoctorSerializer(serializers.ModelSerializer):
    specialty = CategorySerializer()
    user = CustomUserSerializer(many=False)
    class Meta:
        model = DoctorProfile
        fields = [
            'id', 'user', 'specialty', 'experience_years', 'rating',
            'reviews_count', 'consultation_cost', 'description',
            'education', 'treatment_approach', 'experience', 'skills'
        ]
        
class PatientSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(many=False)
    class Meta:
        model = PatientProfile
        fields = '__all__'
        
class ReviewsSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(many = False)
    class Meta:
        model = Reviews
        fields = '__all__'