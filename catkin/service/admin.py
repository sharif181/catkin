from django.contrib import admin
from .models import Feature, Technology, Category, Service

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass