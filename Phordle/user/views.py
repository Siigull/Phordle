from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from feed.models import Image

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', { 'form': form}) 
    elif request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('feed:feed')
        else:
            return render(request, 'user/register.html', {'form': form})

class SignIn(LoginView):
    template_name = 'user/login.html'
    next_page = 'theme:quickstart'

def sign_out(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return HttpResponse()

class Profile(generic.ListView):
    template_name = 'user/profile.html'
    context_object_name = 'user_profile_images'

    def get_queryset(self):
        return Image.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")

def sign_in_anon(request):
    return redirect('image_upload')
        