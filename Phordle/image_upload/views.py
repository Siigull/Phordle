from django.shortcuts import render, redirect
from django.views import generic
from .forms import ImageForm

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(index)
    else:
        initial_data = {'object': 'kys <3'}
        form = ImageForm(initial=initial_data)
        context = {
            'form': form
        }
    return render(request, 'image_upload/upload_image.html', context)