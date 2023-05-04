from django.urls import path, include
from rest_framework import routers

from .views import (
    ClientReviewViewsets
)

router = routers.DefaultRouter()
router.register(r'client-review', ClientReviewViewsets)

urlpatterns = [
    path('', include(router.urls))
]