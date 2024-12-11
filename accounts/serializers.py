from rest_framework import serializers
from .models import *

class userLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
class userVerifyOtpSerializer(serializers.Serializer):
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
        
class patientSeriallizer(serializers.ModelSerializer):
    user_data = UserSerializer(source=user)
    insurance = InsuranceSerializer(source=insurance)
    class Meta:
        model = PatientProfile
        fields = ["user_data", "insurance", "age", "gender", "address", "phone_number"]
        