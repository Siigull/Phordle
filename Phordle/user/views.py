from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView

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
    next_page = 'feed:feed'
    