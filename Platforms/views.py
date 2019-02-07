from rest_framework import generics
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Platforms
from .serializers import PlatformsSerializer
# Create your views here.


class PlatformsListCreate(generics.ListCreateAPIView):
    queryset = Platforms.objects.all()
    serializer_class = PlatformsSerializer


class PlatformsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platforms.objects.all()
    serializer_class = PlatformsSerializer
