from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="media/")
    name = models.CharField(max_length=30)
    is_volunteer = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15)