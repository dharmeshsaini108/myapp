from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=200)
    college=models.CharField(max_length=200)
    age=models.IntegerField() #we have removed the max_length from here b/c it is a barrier in making migrations during mysql databases
    isActive=models.BooleanField(default=False)  