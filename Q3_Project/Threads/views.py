from rest_framework import generics

from .models import Threads
from .serializers import ThreadsSerializer
# Create your views here.


class ThreadsListCreate(generics.ListCreateAPIView):
    queryset = Threads.objects.all()
    serializer_class = ThreadsSerializer
