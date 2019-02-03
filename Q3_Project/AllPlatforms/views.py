from rest_framework import generics
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import AllPlatforms
from .serializers import AllPlatformsSerializer
# Create your views here.


class AllPlatformsListCreate(generics.ListCreateAPIView):
    queryset = AllPlatforms.objects.all()
    serializer_class = AllPlatformsSerializer


class AllPlatformsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AllPlatforms.objects.all()
    serializer_class = AllPlatformsSerializer
