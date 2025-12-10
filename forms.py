# writerapp/forms.py
from django import forms
from .models import Project, Source

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter project name", "class": "input", "style":"width:100%;padding:8px;"})
        }
        labels = {"title": "Project name"}


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ["title", "source_type", "raw_text"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Source title", "style":"width:100%;padding:6px;"}),
            "raw_text": forms.Textarea(attrs={"rows":4, "style":"width:100%;"}),
        }
