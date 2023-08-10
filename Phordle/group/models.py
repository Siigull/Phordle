from django.db import models
from theme.models import Theme
from django.conf import settings

class Group(models.Model):
    name = models.CharField(max_length=25, default="")
    theme = models.OneToOneField(Theme, on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)