from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from Doctors.serializers import DoctorProfileSerializer 
from Doctors.models import DoctorProfile
from .serializers import DoctorSerializer


class DoctorsListView(generics.ListAPIView):
    """
    API view to list all doctors with their profiles, departments, and specialties.
    """
    queryset = DoctorProfile.objects.select_related(
        'user', 'department'  
    ).prefetch_related(
        'specialties'  
    )
    serializer_class = DoctorProfileSerializer
