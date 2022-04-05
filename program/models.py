from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Program(models.Model):
    #relations
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    #fields
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.name
    
class Lecture(models.Model):
    #relations
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    #fields
    name = models.CharField(max_length=50)
    index = models.IntegerField()

    def __str__(self):
        return self.name

class Content(models.Model):
    #relations
    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE)
    #fields
    text = models.TextField()
    video = models.URLField(max_length=200)

class Comment(models.Model):
    #relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    replay = models.ForeignKey("Comment", on_delete=models.CASCADE)
    #fields
    comment = models.CharField(max_length=50)

