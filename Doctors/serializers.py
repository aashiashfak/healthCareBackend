from rest_framework import serializers
from .models import *
from accounts.serializers import UserSerializer
from accounts.models import CustomUser

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

class DoctorProfileSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(
        slug_field='name', queryset=Department.objects.all()
    )
    specialties = serializers.SlugRelatedField(
        slug_field='name', queryset=Specialty.objects.all(), many=True
    )
    user = UserSerializer()

    class Meta:
        model = DoctorProfile
        fields = '__all__'

    def validate(self, data):
        """
        Validate that the user and related data are consistent.
        """
        department = data.get('department')
        specialties = data.get('specialties')

        if not department:
            raise serializers.ValidationError("Department is required.")
        
        if not specialties:
            raise serializers.ValidationError("At least one specialty is required.")

        return data

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        department = validated_data.pop('department')
        specialties = validated_data.pop('specialties')

        # Create user
        email = user_data.pop('email')
        user_data['role'] = 'Doctor'
        user = CustomUser.objects.create_user(email=email, **user_data)

        # Create doctor profile
        doctor = DoctorProfile.objects.create(
            user=user,
            department=department,
            **validated_data
        )
        doctor.specialties.set(specialties)
        return doctor
