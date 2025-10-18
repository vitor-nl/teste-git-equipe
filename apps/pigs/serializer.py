from .models import Pig
from rest_framework import serializers

class PigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pig
        fields = '__all__'