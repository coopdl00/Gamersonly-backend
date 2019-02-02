from django.db import models
from datetime import datetime
from Users.models import Users

class Threads(models.Model):
    thread_creator_user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    thread_name = models.CharField(max_length=200)
    thread_creation_date = models.DateTimeField(default=datetime.now, blank=True)


# Create your models here.
