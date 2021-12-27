from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields='__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permission
        fields='__all__'

class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContentType
        fields='__all__'

