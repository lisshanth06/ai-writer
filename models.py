# writerapp/models.py
from django.db import models
from django.utils import timezone

SOURCE_TYPE_CHOICES = [
    ("text", "Text"),
    ("web", "Web"),
    ("audio", "Audio"),
]

class Project(models.Model):
    title = models.CharField(max_length=255)
    document = models.TextField(blank=True, help_text="Plain text document content")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title


class Source(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="sources")
    title = models.CharField(max_length=255)
    source_type = models.CharField(max_length=10, choices=SOURCE_TYPE_CHOICES, default="text")
    raw_text = models.TextField(help_text="Source text (paste / web summary / transcription)")
    meta = models.JSONField(default=dict, blank=True, help_text="Optional metadata (url, filename, etc.)")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.project.title})"
