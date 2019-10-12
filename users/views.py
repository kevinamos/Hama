# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import status
from users.models import *
from users.serializers import UserSerializer

# Create your views here.

class UserViewset(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )

    @list_route(methods=['get'])
    def user_roles(self, request):
        roles = [role for role in registered_roles]
        return Response(roles)