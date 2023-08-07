from django.db import models

class Image(models.Model):
    object = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images/')
