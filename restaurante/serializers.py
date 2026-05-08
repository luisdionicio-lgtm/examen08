from rest_framework import serializers
from .models import Plato, Pedido


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'precio', 'categoria']


class PedidoSerializer(serializers.ModelSerializer):
    platos_detalle = PlatoSerializer(source='platos', many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'fecha', 'total', 'estado', 'platos', 'platos_detalle']  
             
class PlatoSerializer(serializers.ModelSerializer):
    pedidos_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        source='pedidos'
    )

    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'precio', 'categoria', 'pedidos_ids']