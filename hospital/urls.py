from django.urls import path
from .views import *

urlpatterns = [
    path("list-hospital-doctors/<int:hospital_id>/", ListDoctorsOfHospitalView.as_view(), name="list_hospital_doctors"),
]
