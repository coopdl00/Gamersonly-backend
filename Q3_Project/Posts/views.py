from rest_framework import generics

from .models import Posts
from .serializers import PostsSerializer
# Create your views here.


class PostsListCreate(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
