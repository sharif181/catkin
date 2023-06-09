from django.urls import path, include
from rest_framework import routers

from .views import (
    ContactUsViewSet
)

router = routers.DefaultRouter()
router.register(r'contact-us', ContactUsViewSet)

urlpatterns = [
    path('', include(router.urls))
]