from django_filters import rest_framework as filters
from Doctors.models import DoctorProfile

class DoctorProfileFilter(filters.FilterSet):
    """
    Custom filter class for DoctorProfile.
    """
    department = filters.CharFilter(field_name='department__name', lookup_expr='icontains')
    specialty = filters.CharFilter(field_name='specialties__name', lookup_expr='icontains')

    class Meta:
        model = DoctorProfile
        fields = ['department', 'specialty']
