# writerapp/forms.py
from django import forms
from .models import Source

class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ["title", "source_type", "raw_text", "meta"]
        widgets = {
            "raw_text": forms.Textarea(attrs={"rows": 6}),
            "meta": forms.Textarea(attrs={"rows": 2}),
        }
