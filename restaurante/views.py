from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Plato, Pedido
from .serializers import PlatoSerializer, PedidoSerializer


class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre', 'categoria']


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['estado', 'platos__nombre', 'platos__categoria']