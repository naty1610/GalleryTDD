from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    photo = models.ImageField(max_length=600, null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    educationLevel = models.CharField(max_length=50, blank=True)
    profession = models.CharField(max_length=50, blank=True)

class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)
    profile = models.CharField(max_length=5)
    user = models.ForeignKey(Usuario, null=True, on_delete=models.PROTECT)
