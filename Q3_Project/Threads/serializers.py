from rest_framework import serializers
from .models import Threads
# from Users.models import Users
# from Users.serializers import UsersSerializer

class ThreadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threads
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Users
#         fields = '__all__'
