from django.db import models

# Create your models here.
class Questions(models.Model):
    #relations
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    #fields

    def __str__(self):
        return self.question