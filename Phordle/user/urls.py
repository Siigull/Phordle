from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.SignIn.as_view(), name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('anon/', views.anon_sign_up, name='anon_sign_up'),
]