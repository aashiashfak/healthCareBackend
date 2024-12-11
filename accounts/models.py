from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
from django.utils.translation import gettext_lazy as _

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
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email' 
    
    def __str__(self):
        return f"{self.username} ({self.role})"
