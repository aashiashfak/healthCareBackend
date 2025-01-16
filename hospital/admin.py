from django.contrib import admin
from .models import HospitalProfile
@admin.register(HospitalProfile)
class HospitalProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "short_name",
    ) 
    search_fields = ("user__username", )  
