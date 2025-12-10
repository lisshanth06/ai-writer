# writerapp/urls.py
from django.urls import path
from . import views

app_name = "writerapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("project/new/", views.new_project, name="new_project"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),

    # HTMX fragments & actions
    path("project/<int:pk>/fragment/document/", views.project_document_fragment, name="fragment_document"),
    path("project/<int:pk>/fragment/sources/", views.project_sources_fragment, name="fragment_sources"),
    path("project/<int:pk>/save-document/", views.save_document, name="save_document"),
    path("project/<int:pk>/sources/create/", views.create_source, name="create_source"),
]
