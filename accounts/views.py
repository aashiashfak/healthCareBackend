from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from utils.utils import generate_otp , send_otp_email
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status, generics

class UserLoginAPIview(APIView):
    def post(self, request):
        serializer = userLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            cache_key = f"otp_{email}"  
            existing_otp = cache.get(cache_key)

            if not existing_otp:
                otp = generate_otp()
                cache.set(cache_key, otp, timeout=120)
            else:
                otp = existing_otp
            username = email.split('@')[0]

            print("generated_otp", otp)
            try:
                send_otp_email(email, username, otp)
                return Response({"message": "OTP sent successfully."}, status=status.HTTP_200_OK)
            except Exception as e:
                cache.delete(cache_key)
                return Response(
                    {"error": "Failed to send OTP. Please try again later."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
