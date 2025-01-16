from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets , permissions
from django.db import transaction
from Doctors.models import Department, Specialty, DoctorProfile
from accounts.models import CustomUser
from Doctors.serializers import DoctorProfileSerializer
from accounts.permissions import IsAdmin , IsAdminOrReadOnly
from Doctors.models import Department, Specialty
from Doctors.serializers import DepartmentSerializer, SpecialtySerializer
from hospital.models import HospitalProfile
from hospital.serializers import HospitalProfileSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Department CRUD operations.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    permission_classes = [IsAdminOrReadOnly]

class SpecialtyViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Specialty CRUD operations.
    """
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer

    permission_classes = [IsAdminOrReadOnly]


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


class CreateRetrieveHospitalsAPIView(APIView):
    """
    API endpoint for creating a new hospital and retrieving all hospitals.
    """

    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        """
        Retrieve all hospital profiles.
        """
        queryset = HospitalProfile.objects.select_related('user').prefetch_related('user__address').all()
        serializer = HospitalProfileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new hospital profile.
        """
        serializer = HospitalProfileSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    hospital_profile = serializer.save()
                return Response(
                    {
                        "message": "Hospital created successfully",
                        "data": HospitalProfileSerializer(hospital_profile).data,
                    },
                    status=status.HTTP_201_CREATED,
                )
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
