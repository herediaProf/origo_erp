import io
import qrcode
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Mesa, Pedido, Produto
from .serializers import PedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


def pedidos_dashboard_view(request):
    """Renderiza o painel de métricas e controle do ERP."""
    total_pedidos = Pedido.objects.count()
    total_produtos = Produto.objects.count()
    total_mesas = Mesa.objects.count()

    context = {
        "total_pedidos": total_pedidos,
        "total_produtos": total_produtos,
        "total_mesas": total_mesas,
    }
    return render(request, "pedidos/dashboard.html", context)
