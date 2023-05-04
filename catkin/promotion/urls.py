from django.urls import path, include
from rest_framework import routers

from .views import (
    PromotionViewsets
)

router = routers.DefaultRouter()
router.register(r'promotion', PromotionViewsets)

urlpatterns = [
    path('', include(router.urls))
]