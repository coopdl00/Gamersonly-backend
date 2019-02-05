from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Threads
from Users.models import Users
from .serializers import ThreadsSerializer
from Users.serializers import UsersSerializer
from django.contrib.auth.models import User

# Create your views here.

class ThreadsListCreate(generics.ListCreateAPIView):
    queryset = Threads.objects.all()
    serializer_class = ThreadsSerializer


class ThreadsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Threads.objects.all()
    serializer_class = ThreadsSerializer


# class UsersViewSet(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
