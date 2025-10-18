from django.shortcuts import render
from rest_framework import viewsets
from .models import Lion
from .serializer import LionSerializer

# Create your views here.
class LionViewSet(viewsets.ModelViewSet):
    queryset = Lion.objects.all()
    serializer_class = LionSerializer