from django.db import models
from datetime import datetime
from Users.models import Users

class Platforms(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

# Create your models here.
