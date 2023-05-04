from .serializers import (
    ProjectImageSerializer,
    ProjectSerializer
)
from .models import (
    ProjectImage, 
    Project
)
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response



class ProjectImageViewsets(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TotalProjectCountView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        print(request.META.get('USERNAME'))
        print(request.META.get('HTTP_USER_AGENT'))
        # print(request.META.keys())
        count = Project.objects.all().count()
        return Response({"total_project": count})