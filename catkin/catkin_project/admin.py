from django.contrib import admin
from .models import ProjectImage, Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    pass