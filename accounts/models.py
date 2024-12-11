from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Staff', 'Administrative Staff'),
        ('Admin', 'Hospital Administrator'),
    ]
    username = models.CharField(max_length=25, default="guest")
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    objects = CustomUserManager()
    
    @property
    def tokens(self) -> dict[str,str]:
        print('reached in gen tokens')
        
        referesh = RefreshToken.for_user(self)
        
        return{
           'refresh': str(referesh),
            'access': str(referesh.access_token),
        } 

    USERNAME_FIELD = 'email' 
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    
class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="patient_profile")
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    blood_group = models.CharField(max_length=3, null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=15)
    
    def __str__(self):
        return f"PatientProfile for {self.user.username.upper()}"

class InsurancePolicy(models.Model):
    patient = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, related_name="insurance")
    name = models.CharField(max_length=255)  
    insurance_number = models.CharField(max_length=50, unique=True)  
    start_date = models.DateField()  
    end_date = models.DateField()  

    def __str__(self):
        return f"{self.name} ({self.insurance_number})"



    
    
    
    