from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.

from .forms import ThemeForm, ImageForm
from .models import Theme
from feed.models import Image

# from cloud_vision import object_in_photo


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


global_word_state = {}

class Quickstart(ListView):
    template_name = 'theme/quickstart.html'
    context_object_name = 'quickstart_list'

    def get_queryset(self):
        return Theme.objects.filter(pub_date__lte=timezone.now()).order_by("pub_date")[:3]
    
def create_theme(request):
    if request.method == 'GET':
        form = ThemeForm()
        return render(request, 'theme/create_theme.html', { 'form': form}) 
    elif request.method == 'POST':
        form = ThemeForm(request.POST) 
        if form.is_valid():
            theme = form.save(commit=False)
            theme.save()
            messages.success(request, 'You have created the theme successfully.')
            return HttpResponseRedirect(reverse('theme:theme', args = (theme.id,)))
        else:
            return render(request, 'theme/create_theme.html', {'form': form})
        
def theme_view(request, pk):
    if request.user.id not in global_word_state:
        global_word_state[request.user.id] = {'word_0':False, 'word_1':False, 'word_2':False}

    if request.method == 'GET':
        form = ImageForm()
        theme = Theme.objects.get(pk=pk)

        return render(request, 'theme/theme.html', {'form': form, 'theme': theme, 'words': global_word_state[request.user.id] }) 
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        theme = Theme.objects.get(pk=pk)

        image = Image.objects.filter(pub_date__lte=timezone.now()).last().image.read()

        result = object_in_photo(image)

        found = []

        for i in result:
            found.append(i.description)
            if i.description == theme.word_0:
                global_word_state[request.user.id]['word_0'] = True
                return HttpResponseRedirect(reverse('theme:theme', args = (theme.id,)))
            elif i.description == theme.word_1:
                global_word_state[request.user.id]['word_1'] = True
                return HttpResponseRedirect(reverse('theme:theme', args = (theme.id,)))
            elif i.description == theme.word_2:
                global_word_state[request.user.id]['word_2'] = True
                return HttpResponseRedirect(reverse('theme:theme', args = (theme.id,)))
            
        form = ImageForm()
        return render(request, 'theme/theme.html', {'form': form, 'theme': theme, 'words': global_word_state[request.user.id], 'found': found})


        
        
        