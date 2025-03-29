from rest_framework import serializers
from .models import Igreja

class IgrejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Igreja
        fields = '__all__'
