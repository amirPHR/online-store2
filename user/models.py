from django.db import models 
from django.conf import settings
from django.contrib.auth.models import AbstractUser 

# User Model 
class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='Phone Number')

    def check_phone_number(self):
        """
        This function checks:
        - Phone number only digits 
        - Len of Phone number just 11 digits
        """
        if not self.phone_number.isdigit():
            raise ValueError('Phone number most contain only digits')
        if len(self.phone_number) != 11:
            raise ValueError('Your Phone number is not 11 digits') 
        return True 
    
    def __str__(self):
        return f'username: {self.username}'

# UserProfile Model 
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10, unique=True, verbose_name='National Code') 
    address = models.TextField(verbose_name='Address')
    birth_date = models.DateField(verbose_name='Birth Date', blank=True) 
    job = models.CharField(max_length=255, verbose_name='Job', blank=True)  
    
    def check_national_code(self):
        """
        This function checks:
        - National code only digits
        - Len of National code just 10 digits
        """
        if not self.national_code.isdigit():
            raise ValueError('National code most contain digits') 
        if len(self.national_code) != 10:
            raise ValueError('Your National code is not 10 digits')
        return True

    def __str__(self):
        return f'username: {self.user.username}'