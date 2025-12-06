# writerapp/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Project
from .forms import SourceForm

def home(request):
    projects = Project.objects.all()
    return render(request, "writerapp/home.html", {"projects": projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = SourceForm()
    return render(request, "writerapp/project_detail.html", {"project": project, "form": form})

def create_source(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = SourceForm(request.POST)
        if form.is_valid():
            src = form.save(commit=False)
            src.project = project
            src.save()
            # In future: compute embeddings / index into Qdrant here and save point id to src.meta
            if request.headers.get("HX-Request") == "true":  # HTMX request
                return render(request, "writerapp/includes/sources_table.html", {"project": project})
            return redirect(reverse("writerapp:project_detail", args=(project.pk,)))
    return redirect(reverse("writerapp:project_detail", args=(project.pk,)))
