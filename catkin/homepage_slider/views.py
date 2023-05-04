from rest_framework import viewsets
from .serializers import HomePageSliderSerializer
from .models import HomePageSlider
from rest_framework import permissions


class HomePageSliderViewSet(viewsets.ModelViewSet):
    queryset = HomePageSlider.objects.all()
    serializer_class = HomePageSliderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]