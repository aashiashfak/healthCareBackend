from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(DoctorProfile)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'department', 'qualifications', 'years_of_experience', 'end_time', 'start_time', 'off_days', )

@admin.register(Department)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

@admin.register(Specialty)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

