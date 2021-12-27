from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from Permission.permission import AnyPermissions
from user.models import User
from user.serializers import UserSerializer, PermissionSerializer, GroupSerializer, ContentTypeSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AnyPermissions,)


class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionView(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class ContentTypeView(viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer

    # def list(self,request):
    #     queryset=Permission.objects.all()
    #     serializer=PermissionSerializer(queryset,many=True)
    #
    #     return Response(serializer.data)