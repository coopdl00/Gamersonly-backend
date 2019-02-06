from rest_framework import generics
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Posts
from .serializers import PostsSerializer
# Create your views here.


class PostsListCreate(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
