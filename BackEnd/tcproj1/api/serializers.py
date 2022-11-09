from rest_framework import serializers
from . models import TcData

class TcDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcData
        fields = '__all__'