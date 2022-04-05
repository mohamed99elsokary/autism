from django.db import models

# Create your models here.
class Research(models.Model):

    pdf = models.FileField(upload_to="media/", max_length=100)