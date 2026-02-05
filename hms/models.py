
from django.db import models

# Create your models here.

class Patient(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.IntegerField()
    phone_number = models.IntegerField()
    address = models.TextField()


class doctor(models.Model):
    name = models.CharField(max_length=200)
    userid = models.IntegerField()
    password = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    address = models.TextField()
