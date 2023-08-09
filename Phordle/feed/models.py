from django.db import models
from django.utils import timezone

class Image(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    object = models.CharField(max_length=50, default='', null=True)
    image = models.ImageField(upload_to = 'images/')
    likes = models.IntegerField(default=0, null=True)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    # user = User()