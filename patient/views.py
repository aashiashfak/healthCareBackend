from rest_framework import generics, filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from Doctors.serializers import DoctorProfileSerializer
from Doctors.models import DoctorProfile
from hospital.models import HospitalProfile
from hospital.serializers import HospitalProfileSerializer
from .filters import DoctorProfileFilter
import inspect
class DoctorsListView(generics.ListAPIView):
    """
    API view to list all doctors with their profiles, departments, and specialties.
    Includes filtering and searching capabilities using a filter class.
    """
    queryset = DoctorProfile.objects.select_related(
        'user', 'department'
    ).prefetch_related(
        'specialties'
    )
    serializer_class = DoctorProfileSerializer

    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter]

    filterset_class = DoctorProfileFilter
    search_fields = ['user__username',  'department__name', 'specialties__name']

class HospitalsListView(generics.ListAPIView):
    """
    API view to list all hospitals with their profiles
    """
    queryset = HospitalProfile.objects.select_related('user').prefetch_related('user__address')
    serializer_class = HospitalProfileSerializer
    filter_backends = [drf_filters.SearchFilter]
    search_fields = [
        "user__username",
        "short_name",
        "user__address__city",
        "user__address__street_name_1",
        "user__address__street_name_2",
        "user__address__state",
    ]
