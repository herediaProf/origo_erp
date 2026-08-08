from rest_framework import viewsets
from .models import Mesa, Pedido, ItemPedido
from produtos.models import Produto
from .serializers import (
    MesaSerializer,
    ProdutoSerializer,
    PedidoSerializer,
    ItemPedidoSerializer,
)


class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.filter(disponivel=True)
    serializer_class = ProdutoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
