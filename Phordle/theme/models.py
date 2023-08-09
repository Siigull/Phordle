from django.db import models

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=50)
    word_0 = models.CharField(default="", max_length=100)
    word_1 = models.CharField(default="", max_length=100)
    word_2 = models.CharField(default="", max_length=100)
    public = models.BooleanField(default=True)
    pub_date = models.DateTimeField("date published", default="1970-01-01")