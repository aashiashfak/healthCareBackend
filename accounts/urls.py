from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('sign-in/', UserLoginAPIview.as_view(), name='user_sign_up'),
]
