from django.shortcuts import render
from django.views import generic
from django.utils import timezone

# Create your views here.

from .models import Image

class FeedView(generic.ListView):
    template_name = "feed/index.html"
    context = "list of todays most popular images images"
    context_object_name = "latest_image_list"

    def get_queryset(self):
        return Image.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:10]