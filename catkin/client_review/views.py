
from .serializers import ClientReviewSerializer
from .models import ClientReview
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser



class ClientReviewViewsets(viewsets.ModelViewSet):
    queryset = ClientReview.objects.all()
    serializer_class = ClientReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)