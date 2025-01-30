from django.shortcuts import render
from rest_framework import generics
from Doctors.serializers import DoctorProfileSerializer
from Doctors.models import DoctorProfile


class ListDoctorsOfHospitalView(generics.ListAPIView):
    serializer_class = DoctorProfileSerializer

    def get_queryset(self):
        hospital_id = self.kwargs["hospital_id"]
        print(hospital_id)
        return (
            DoctorProfile.objects.select_related("user", "department")
            .prefetch_related("specialties")
            .filter(hospital=hospital_id)
        )
