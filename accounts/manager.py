from django.contrib.auth.models import  BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager): 
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        if password:  
            user.set_password(password)
        else:  
            raise ValueError(_('The Email field must be set'))
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None,  **extra_fields):
        user = self.create_user(email, password=password,)
        user.is_superuser = True  
        user.is_staff = True 
        user.role='Admin'
        user.save(using=self._db)
        return user