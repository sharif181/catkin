from django.contrib import admin
from .models import ContactUs

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    pass