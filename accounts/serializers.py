from rest_framework import serializers
from .models import *

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
class UserVerifyOtpSerializer(serializers.Serializer):
    email    = serializers.EmailField(required=True)
    otp      = serializers.CharField(required=True, min_length=6, max_length=6)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model    = CustomUser
        fields   = ['id', 'email', 'role', 'is_verified', 'username', 'phone_number']
        
class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = "__all__"
        
class PatientSeriallizer(serializers.ModelSerializer):
    user_data = UserSerializer()
    class Meta:
        model = PatientProfile
        fields = ["user_data", "gender", "address", "blood_group", "allergies", "emergency_contact_number" ]

class PatientSignUpSerializer(serializers.Serializer):
    otp      = serializers.CharField(required=True, min_length=6, max_length=6)
    patient = PatientSeriallizer()