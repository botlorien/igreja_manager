from rest_framework import serializers
from .models import Comprovante

class ComprovanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprovante
        fields = '__all__'
