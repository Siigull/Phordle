from django.urls import path

from . import views

app_name = "theme"
urlpatterns = [ path("quickstart/", views.Quickstart.as_view(), name="quickstart"),
                path("create_theme", views.create_theme, name="create_theme"),
                path("<int:pk>/", views.ThemeView.as_view(), name="theme")]