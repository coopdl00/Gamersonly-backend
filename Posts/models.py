from django.db import models
from datetime import datetime
from Users.models import Users
from Threads.models import Threads

class Posts(models.Model):
    poster_user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    thread_id = models.ForeignKey(Threads, on_delete=models.DO_NOTHING)
    post_description = models.TextField(blank=True)
    post_creation_date = models.DateTimeField(default=datetime.now, blank=True)


# Create your models here.
