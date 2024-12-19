from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('create-doctor/', CreateDoctorsAPIView.as_view(), name='create_doctor'),
]

#viewset routers
router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'specialties', SpecialtyViewSet, basename='specialty')

urlpatterns = router.urls
