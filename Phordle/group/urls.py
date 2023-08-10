from django.urls import path

from . import views

app_name = "group"
urlpatterns = [ path("create_group/", views.create_group, name="create_group")]