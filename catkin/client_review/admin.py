from django.contrib import admin
from .models import ClientReview

@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    pass