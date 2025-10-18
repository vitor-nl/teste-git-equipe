from rest_framework import viewsets
from .models import Frog
from .serializer import FrogSerializer

class FrogViewSet(viewsets.ModelViewSet):
    queryset = Frog.objects.all()
    serializer_class = FrogSerializer  