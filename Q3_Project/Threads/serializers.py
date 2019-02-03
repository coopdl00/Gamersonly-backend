from rest_framework import serializers
from .models import Threads


class ThreadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threads
        fields = '__all__'
