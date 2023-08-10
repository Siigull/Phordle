from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User

from feed.models import Image
from group.models import Group

################ random name for anon generator
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
################

def anon_sign_up(request):
    s = get_random_string(10)
    username = f"anon{s}"
    password = f"anon{s}"
    email = f"anon{s}"

    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()
    login(request, user)
    return redirect('theme:quickstart')

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
    return redirect('feed:feed')

class Profile(generic.ListView):
    template_name = 'user/profile.html'
    context_object_name = 'user_profile_groups'

    def get_queryset(self):
        return Group.objects.filter(users=self.request.user.id).all()

def sign_in_anon(request):
    return redirect('image_upload')
        