from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import JSONField

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Specialty Model
class Specialty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# DoctorProfile Model
class DoctorProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    specialties = models.ManyToManyField('Specialty')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    off_days = JSONField(default=list)  # e.g., ['sunday', 'monday']
    shift_schedule = JSONField(default=list)  # e.g., ['3am-5am', '4pm-6pm']
    years_of_experience = models.PositiveIntegerField()
    qualifications = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Doctor Profile of {self.user.username.upper()}"
