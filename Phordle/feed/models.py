from django.db import models
from django.utils import timezone

class Image(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default='1970-01-01')
    image = models.ImageField(upload_to = 'images/')
    # user = User()

    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        super(Image, self).save(*args, **kwargs)