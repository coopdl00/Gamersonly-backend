from django.db import models
from datetime import datetime

class Users(models.Model):
    screen_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    profile_picture = models.CharField(max_length=500)
    about_me = models.TextField(blank=True)
    

# Create your models here.
