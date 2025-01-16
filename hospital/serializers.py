from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import HospitalProfile


class HospitalProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = HospitalProfile
        fields = "__all__"

    # def validate(self, data):
    #     if data["user"]["role"] != "Hospital":
    #         raise serializers.ValidationError("User role must be 'Hospital'.")
    #     return data

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
            hospital_profile = HospitalProfile.objects.create(
                user=user, **validated_data
            )
            return hospital_profile
