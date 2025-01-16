from rest_framework import serializers
from .models import *


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class UserVerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True, min_length=6, max_length=6)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["street_name_1", "street_name_2", "city", "state", "pincode"]


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField()
    address = AddressSerializer()

    class Meta:
        model = CustomUser
        fields = ["id", "email", "role", "is_verified", "username", "phone_number", 'address']

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        address, created = Address.objects.get_or_create(**address_data) 
        user = CustomUser.objects.create(address=address, **validated_data)
        return user

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = "__all__"


class PatientSeriallizer(serializers.ModelSerializer):
    user_data = UserSerializer()

    class Meta:
        model = PatientProfile
        fields = [
            "user_data",
            "gender",
            "address",
            "blood_group",
            "allergies",
            "emergency_contact_number",
        ]


class PatientSignUpSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True, min_length=6, max_length=6)
    patient = PatientSeriallizer()
