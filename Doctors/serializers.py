from rest_framework import serializers
from .models import *
from accounts.serializers import UserSerializer
from accounts.models import CustomUser

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'description']
        
class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

class DoctorProfileSerializer(serializers.ModelSerializer):
    department = serializers.CharField()
    specialties = serializers.ListField(child=serializers.CharField())
    user = UserSerializer()

    class Meta:
        model = DoctorProfile
        fields = '__all__'

    def validate_department(self, value):
        """
        Ensure the provided department exists by name.
        """
        if not Department.objects.filter(name=value).exists():
            raise serializers.ValidationError(f"Department '{value}' does not exist.")
        return value

    def validate_specialties(self, value):
        """
        Ensure all provided specialties exist by name.
        """
        specialties = []
        for specialty_name in value:
            try:
                specialty = Specialty.objects.get(name=specialty_name)
                specialties.append(specialty)
            except Specialty.DoesNotExist:
                raise serializers.ValidationError(f"Specialty '{specialty_name}' does not exist.")
        return specialties

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        department_name = validated_data.pop('department')
        specialties_data = validated_data.pop('specialties') 

        email = user_data.pop('email')
        user_data['role'] = 'Doctor'
        user = CustomUser.objects.create_user(email=email, **user_data)

        department = Department.objects.get(name=department_name)

        doctor = DoctorProfile.objects.create(
            user=user,
            department=department,
            **validated_data
        )
        doctor.specialties.set(specialties_data)
        return doctor