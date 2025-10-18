from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer
# Create your views here.
class HorseViewSet(viewsets.ModelViewSet):
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer