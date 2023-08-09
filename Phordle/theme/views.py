from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .forms import ThemeForm
from .models import Theme

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
            return render(request, 'theme/create_theme.html', { 'form': form})
        
class ThemeView(DetailView):
    model=Theme
    template_name="theme/theme.html"

    # context_object_name = 'q'