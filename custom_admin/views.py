from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from Doctors.models import Department, Specialty, DoctorProfile
from accounts.models import CustomUser
from Doctors.serializers import DoctorProfileSerializer
from accounts.permissions import IsAdmin

class CreateDoctorsAPIView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        serializer = DoctorProfileSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    serializer.save()
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'message': 'Doctor created successfully'}, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)