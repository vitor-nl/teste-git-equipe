from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Ducks
from .serializer import DucksSerializer


class DucksViewSet(viewsets.ModelViewSet):
    queryset = Ducks.objects.all()
    serializer_class = DucksSerializer  