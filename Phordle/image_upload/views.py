from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone

from .forms import ImageForm
from feed.models import Image

################### cloud-vision because import from another file didnt work
from google.cloud import vision
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('theme/top-chain-394711-21fa8ce1fe35.json')

client = vision.ImageAnnotatorClient(credentials=credentials)

def object_in_photo(content):
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    return response.label_annotations
###################

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        image = Image.objects.filter(pub_date__lte=timezone.now()).last().image.read()

        result = object_in_photo(image)

        labels = []
        
        form = ImageForm()

        for i in result:
            labels.append(i.description)

        return render(request, 'image_upload/upload_image.html', {"found": labels, "form": form})
    else:
        form = ImageForm()

    return render(request, 'image_upload/upload_image.html', {"form": form})