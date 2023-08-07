from django.urls import path

from . import views

app_name = "image_upload"
urlpatterns = [ path("", views.index, name="upload")]