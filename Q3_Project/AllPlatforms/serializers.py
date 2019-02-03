from rest_framework import serializers
from .models import AllPlatforms


class AllPlatformsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllPlatforms
        fields = '__all__'
