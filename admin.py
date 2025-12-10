# writerapp/admin.py
from django.contrib import admin
from .models import Project, Source

class SourceInline(admin.TabularInline):
    model = Source
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at", "created_at")
    search_fields = ("title",)
    inlines = [SourceInline]

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "source_type", "created_at")
    list_filter = ("source_type",)
    search_fields = ("title", "raw_text")
