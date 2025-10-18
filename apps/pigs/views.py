from django.shortcuts import render
from rest_framework import viewsets
from .models import Pig
from .serializer import PigSerializer

# Create your views here.

class PigViewSet(viewsets.ModelViewSet):
    queryset = Pig.objects.all()
    serializer_class = PigSerializer  