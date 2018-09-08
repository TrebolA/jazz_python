from rest_framework import serializers
from registro.models import Bogota, Medellin

class BogotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bogota
        fields = ('id', 'nombre', 'apellido', 'correo', 'celular', 'terminos', 'politica')

class MedellinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medellin
        fields = ('id', 'nombre', 'apellido', 'correo', 'celular', 'terminos', 'politica')
