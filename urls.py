# writerapp/urls.py
from django.urls import path
from . import views

app_name = "writerapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("project/<int:pk>/sources/create/", views.create_source, name="create_source"),
]
