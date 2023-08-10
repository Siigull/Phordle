from django.urls import path

from . import views

app_name = "group"
urlpatterns = [ path("create_group/", views.create_group, name="create_group"),
                path("<int:pk>/group", views.group, name="group_info"),
                path("group_list/", views.GroupList.as_view(), name="group_list"),
                path("group_theme/", views.group_theme, name="group_theme") ]