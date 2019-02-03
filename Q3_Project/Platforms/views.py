from rest_framework import generics

from .models import Platforms
from .serializers import PlatformsSerializer
# Create your views here.


class PlatformsListCreate(generics.ListCreateAPIView):
    queryset = Platforms.objects.all()
    serializer_class = PlatformsSerializer
