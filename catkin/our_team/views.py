from django.shortcuts import render
from .serializers import DesignationSerializer, TeamMemberSerializer
from .models import Designation, TeamMember
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response


class DesignationViewsets(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeamMemberViewsets(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)


class TotalPeopleCountView(APIView):

    def get(self, request, *args, **kwargs):
        count = TeamMember.objects.all().count()
        return Response({"our_member": count})