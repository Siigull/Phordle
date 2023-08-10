from django.contrib import admin
from feed.models import Image
from theme.models import Theme
from group.models import Group

# Register your models here.

admin.site.register(Image)
admin.site.register(Theme)
admin.site.register(Group)
