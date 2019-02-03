from rest_framework import serializers
from .models import Platforms


class PlatformsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platforms
        fields = '__all__'
