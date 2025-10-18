from .models import Lion
from rest_framework import serializers

class LionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lion
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']