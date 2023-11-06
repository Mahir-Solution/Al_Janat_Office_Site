from django.db import models
class Office(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    message =  models.TextField()
# Create your models here.
