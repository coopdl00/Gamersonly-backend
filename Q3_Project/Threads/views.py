from rest_framework import generics
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Threads
from .serializers import ThreadsSerializer
# Create your views here.

class ThreadsListCreate(generics.ListCreateAPIView):
    queryset = Threads.objects.all()
    serializer_class = ThreadsSerializer


class ThreadsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Threads.objects.all()
    serializer_class = ThreadsSerializer
