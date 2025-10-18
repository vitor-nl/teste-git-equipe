from .models import Ducks
from rest_framework import serializers

class DucksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ducks
        fields = '__all__'