from django.urls import path
from .views import (
    CreateDoctorsAPIView,
    CreateRetrieveHospitalsAPIView,
    DepartmentViewSet,
    SpecialtyViewSet,
)
from rest_framework.routers import DefaultRouter

# API paths
urlpatterns = [
    path("create-doctor/", CreateDoctorsAPIView.as_view(), name="create_doctor"),
    path(
        "create-retrieve/hospitals/",
        CreateRetrieveHospitalsAPIView.as_view(),
        name="create_retrieve_hospitals",
    ),
]

# ViewSet routers
router = DefaultRouter()
router.register(r"departments", DepartmentViewSet, basename="department")
router.register(r"specialties", SpecialtyViewSet, basename="specialty")

urlpatterns += router.urls
