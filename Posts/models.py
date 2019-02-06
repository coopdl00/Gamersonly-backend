from django.db import models
from datetime import datetime
from Users.models import Users

class Posts(models.Model):
    poster_user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    post_title = models.CharField(max_length=200)
    post_description = models.TextField(blank=True)
    post_creation_date = models.DateTimeField(default=datetime.now, blank=True)


# Create your models here.
