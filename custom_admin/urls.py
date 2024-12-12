from django.urls import path
from .views import *

urlpatterns = [
    path('create-doctor/', CreateDoctorsAPIView.as_view(), name='create_doctor'),
]
