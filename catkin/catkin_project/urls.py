from django.urls import path, include
from rest_framework import routers

from .views import (
    ProjectImageViewsets,
    ProjectViewset,
    TotalProjectCountView
)

router = routers.DefaultRouter()
router.register(r'project-image', ProjectImageViewsets)
router.register(r'project', ProjectViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('total-project', TotalProjectCountView.as_view())
]