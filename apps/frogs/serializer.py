from .models import Frog
from rest_framework import serializers

class FrogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frog
        fields = '__all__'