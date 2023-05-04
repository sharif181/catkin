from django.urls import path, include
from rest_framework import routers

from .views import (
    DesignationViewsets,
    TeamMemberViewsets,
    TotalPeopleCountView
)

router = routers.DefaultRouter()
router.register(r'designation', DesignationViewsets)
router.register(r'team', TeamMemberViewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('total-member', TotalPeopleCountView.as_view())
]
