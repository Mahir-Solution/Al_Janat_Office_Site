#from django.utils import timezone
from django.db import models
class Registration(models.Model):
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    study = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    registration_d = models.CharField(max_length=200, default="Null")
    contact = models.CharField(max_length=50)
    address = models.TextField()
 
# Create your models here.
