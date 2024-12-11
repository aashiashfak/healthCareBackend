from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('sign-in/', UserLoginRequestAPIView.as_view(), name='user_sign_in'),
    path('verify-otp/', UserLoginVerifyAPIView.as_view(), name='verify-otp'),
]
