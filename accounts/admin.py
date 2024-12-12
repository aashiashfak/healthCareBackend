from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_active', 'date_of_birth', 'phone_number', 'created_at', 'updated_at',)
    search_fields = ('email', 'username', 'phone_number')
