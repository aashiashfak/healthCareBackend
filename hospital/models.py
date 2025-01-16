from django.db import models
from accounts.models import CustomUser, Address

class HospitalProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="hospital_profile",
        limit_choices_to={
            "role": "Hospital"
        },  
    )
    short_name = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return f"Hospital: {self.user.username}"
