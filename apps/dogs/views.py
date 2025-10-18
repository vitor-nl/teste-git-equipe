from django.shortcuts import render
from rest_framework import viewsets
from .models import Dog
from .serializer import DogSerializer

# Create your views here.

class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer