from rest_framework import serializers
from accounts.serializers import UserSerializer
from Doctors.models import DoctorProfile


class DoctorSerializer(serializers.ModelField):
    user = UserSerializer()
    class Meta:
        model = DoctorProfile
        fields =  '__all__'
        