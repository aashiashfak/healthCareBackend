from django.urls import path
from .views import *

urlpatterns = [
    path('list-doctors/', DoctorsListView.as_view(), name='list_doctors'),
    path('list-hospitals/', HospitalsListView.as_view(), name='list_hospitals'),
]


