from django.shortcuts import render
from rest_framework import viewsets
from .models import movies

from django.contrib.auth.models import User
from .serializers import moviesSerializer,UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
class moviesViewSet(viewsets.ModelViewSet):
    queryset= movies.objects.all()
    serializer_class = moviesSerializer

