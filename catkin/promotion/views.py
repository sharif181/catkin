from .serializers import PromotionSerializer
from .models import Promotion
from rest_framework import viewsets
from rest_framework import permissions


class PromotionViewsets(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]