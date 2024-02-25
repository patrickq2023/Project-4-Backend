from django.contrib.auth.models import Group, User
from .models import Image
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'name']

class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'



        