# writerapp/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from .models import Project, Source
from .forms import ProjectForm, SourceForm

def home(request):
    projects = Project.objects.all()
    return render(request, "writerapp/home.html", {"projects": projects})


def new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("writerapp:home"))
    else:
        form = ProjectForm()
    return render(request, "writerapp/new_project.html", {"form": form})


def project_detail(request, pk):
    """Main project screen. This view renders the page and the HTMX tabs will load fragments."""
    project = get_object_or_404(Project, pk=pk)
    # initial document and sources fragments will be included in template (no separate HTMX call required)
    source_form = SourceForm()
    return render(request, "writerapp/project_detail.html", {"project": project, "source_form": source_form})


# HTMX fragment: document tab content (so HTMX can request it if desired)
def project_document_fragment(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "writerapp/includes/document_tab.html", {"project": project})


# HTMX fragment: sources tab content
def project_sources_fragment(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "writerapp/includes/sources_tab.html", {"project": project, "source_form": SourceForm()})


# Save document via POST (regular or HTMX)
def save_document(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        new_text = request.POST.get("document", "")
        project.document = new_text
        project.save()
        # If HTMX request, return small fragment for status
        if request.headers.get("HX-Request") == "true":
            return render(request, "writerapp/includes/save_status.html", {"message": "Saved"})
        return redirect(reverse("writerapp:project_detail", args=(pk,)))
    return redirect(reverse("writerapp:project_detail", args=(pk,)))


# Create a source via HTMX (AJAX)
def create_source(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = SourceForm(request.POST)
        if form.is_valid():
            src = form.save(commit=False)
            src.project = project
            src.save()
            # return updated sources table fragment (HTMX will swap it)
            return render(request, "writerapp/includes/sources_table.html", {"project": project})
        # if invalid, re-render the sources tab (with errors)
        return render(request, "writerapp/includes/sources_tab.html", {"project": project, "source_form": form})
    return redirect(reverse("writerapp:project_detail", args=(pk,)))
