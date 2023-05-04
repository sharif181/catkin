from django.urls import path, include
from rest_framework import routers

from .views import (
    FeatureViewsets,
    TechnologyViewsets,
    CatagoryViesets,
    ServiceViewsets
)

router = routers.DefaultRouter()
router.register(r'feature', FeatureViewsets)
router.register(r'technology', TechnologyViewsets)
router.register(r'catagory', CatagoryViesets)
router.register(r'service', ServiceViewsets)

urlpatterns = [
    path('', include(router.urls))
]