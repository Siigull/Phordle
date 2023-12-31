from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Username:", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
    email = forms.EmailField(label="Email:", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter email'}))
    password1 = forms.CharField(label="Password:", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}))
    password2 = forms.CharField(label="Confirm Password:", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')