from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from utils.utils import generate_otp , send_otp_email
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status, generics
from .models import CustomUser
from django.conf import settings

class UserLoginRequestAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserLoginVerifyAPIView(APIView):
    def post(self, request):
        serializer = UserVerifyOtpSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']  
            
            stored_otp = cache.get(f"otp_{email}")
            print('stored_otp', stored_otp, "otp",  otp, end="\n" )
            
            if stored_otp == otp:
                try:
                    user = CustomUser.objects.get(email=email)
                except CustomUser.DoesNotExist:
                    cache.delete(f"otp_{email}")
                    return Response(
                        {"error": "User does not exist."},
                        status=status.HTTP_404_NOT_FOUND
                    )
                
                cache.delete(f"otp_{email}")
                
                tokens = user.tokens 
                user_serializer = UserSerializer(user)

                response = Response({
                    "message": "User verified successfully.",  
                    "user": user_serializer.data,
                    "access": tokens['access']
                }, status=status.HTTP_200_OK)
                
                print(response.data)
                
                refresh_token_expiry = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']

                response.set_cookie(
                    key='refresh',
                    value=tokens['refresh'],
                    httponly=True,
                    secure=False,  
                    samesite='Lax',
                    max_age=int(refresh_token_expiry.total_seconds()),  
                )

                return response
            return Response(
                    {"error": "Invalid OTP or Expired"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientSignUpRequestView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            
            if CustomUser.objects.filter(email=email).exists():
                return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

            cache_key = f"otp_{email}"
            otp = cache.get(cache_key) or generate_otp()
            cache.set(cache_key, otp, timeout=120)
            
            print("generated_otp", otp)
    
            username = email.split('@')[0]

            try:
                send_otp_email(email, username, otp)
                return Response({"message": "OTP sent successfully."}, status=status.HTTP_200_OK)
            except Exception:
                cache.delete(cache_key)
                return Response({"error": "Failed to send OTP. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class PatientSignUpVerifyView(APIView):
    def post(self, request):
        print('patient_data', request.data)
        serializer = PatientSignUpSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['patient']['user_data']['email']
            otp = serializer.validated_data['otp']

            stored_otp = cache.get(f"otp_{email}")
            
            print('stored_otp', stored_otp, "otp",  otp, end="\n" )

            if otp == stored_otp:
                user_data = serializer.validated_data['patient']['user_data']
                user = CustomUser.objects.filter(email=email).first()
                if not user:
                    user_data['role'] = 'Patient'  
                    password = user_data.get('password', None)
                    email = user_data.pop('email')  
                    print('email', email)

                    user = CustomUser.objects.create_user(
                        email=email,
                        password=password, 
                        **user_data
                    )
                    if user:
                        if not hasattr(user, 'patient_profile'):
                            patient_data = serializer.validated_data['patient']
                            patient_profile = PatientProfile.objects.create(
                                user=user,
                                gender=patient_data.get('gender', ''),
                                blood_group=patient_data.get('blood_group', ''),
                                allergies=patient_data.get('allergies', ''),
                                address=patient_data.get('address', ''),
                                emergency_contact_number=patient_data.get('emergency_contact_number', '')
                            )
                            patient_profile.save()
                    tokens = user.tokens 
                    user_serializer = UserSerializer(user)

                    response = Response({
                        "message": "OTP verified and user signed in successfully!",  
                        "user": user_serializer.data,
                        "access": tokens['access']
                    }, status=status.HTTP_200_OK)
                    
                    refresh_token_expiry = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']

                    response.set_cookie(
                        key='refresh',
                        value=tokens['refresh'],
                        httponly=True,
                        secure=False,  
                        samesite='Lax',
                        max_age=int(refresh_token_expiry.total_seconds()),  
                    )

                    return response
                
                return Response({'error':'user already exist'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'Invalid OTP!'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)