from django.db import models

# Create your models here.
class Story(models.Model):
    
    image = models.ImageField(upload_to='media/')
    text = models.TextField()