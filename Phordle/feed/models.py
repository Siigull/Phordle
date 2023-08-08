from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=25)

class Image(models.Model):
    object = models.CharField(max_length=50, default='', null=True)
    image = models.ImageField(upload_to = 'images/')
    likes = models.IntegerField(default=0, null=True)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    # user = User()