from django_filters import rest_framework as filters
from Doctors.models import DoctorProfile

class DoctorProfileFilter(filters.FilterSet):
    """
    Custom filter class for DoctorProfile.
    """
    department = filters.CharFilter(method='filter_department')
    specialty = filters.CharFilter(method="filter_specialty")

    class Meta:
        model = DoctorProfile
        fields = ["department", "specialties"]

    def filter_department(self, queryset, name, value):
        departments = value.split(',')
        return queryset.filter(department__name__in=departments)

    def filter_specialty(self, queryset, name, value):
        specialties = value.split(",")  
        return queryset.filter(specialties__name__in=specialties).distinct()
 