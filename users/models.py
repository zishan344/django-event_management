from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.
class CustomUser(AbstractUser):
    phoneNumber = models.CharField (unique=True,max_length=15,validators=[
            RegexValidator(regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+88011111112221'. Up to 15 digits allowed."
            )])
    profile_image = models.ImageField(
        upload_to='profile_images',blank=True,default='profile_images/default.png'
        )