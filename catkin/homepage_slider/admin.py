from django.contrib import admin
from .models import HomePageSlider

@admin.register(HomePageSlider)
class HomePageSliderAdmin(admin.ModelAdmin):
    pass