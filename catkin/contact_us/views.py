from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactUsSerializer
from .models import ContactUs
from rest_framework import permissions


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.AllowAny]