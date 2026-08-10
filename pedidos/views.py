import io
import qrcode
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Mesa, Pedido, Produto, Funcionario, Fornecedor
from .serializers import PedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


def pedidos_dashboard_view(request):
    """Renderiza o painel unificado de métricas e controle do ERP."""
    context = {
        # Métricas de Pedidos
        "total_pedidos": Pedido.objects.count(),
        "pedidos_pendentes": Pedido.objects.filter(status="PENDENTE").count(),
        # Métricas de Estrutura
        "total_mesas": Mesa.objects.count(),
        # Métricas de Outros Módulos
        "total_produtos": Produto.objects.count(),
        "produtos_baixo_estoque": Produto.objects.filter(
            estoque_atual__lte=5
        ).count(),  # CORRIGIDO AQUI
        "total_funcionarios": Funcionario.objects.filter(ativo=True).count(),
        "total_fornecedores": Fornecedor.objects.count(),
    }
    return render(request, "pedidos/dashboard.html", context)
