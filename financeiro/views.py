from rest_framework import viewsets
from django.shortcuts import render
from django.db.models import Sum
from .models import Caixa, Venda, RateioCaixinha
from .serializers import (
    CaixaSerializer,
    VendaSerializer,
    RateioCaixinhaSerializer,
)


class CaixaViewSet(viewsets.ModelViewSet):
    queryset = Caixa.objects.select_related("operador").prefetch_related("vendas").all()
    serializer_class = CaixaSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.select_related("pedido", "caixa").all()
    serializer_class = VendaSerializer


class RateioCaixinhaViewSet(viewsets.ModelViewSet):
    queryset = RateioCaixinha.objects.select_related("caixa").all()
    serializer_class = RateioCaixinhaSerializer


def financeiro_dashboard_view(request):
    """Renderiza o painel financeiro e de controle de caixa."""
    total_vendas = Venda.objects.aggregate(Sum("valor_total"))["valor_total__sum"] or 0
    caixas_abertos = Caixa.objects.filter(status="aberto").count()
    total_taxa_servico = (
        Venda.objects.aggregate(Sum("valor_taxa_servico"))["valor_taxa_servico__sum"]
        or 0
    )

    context = {
        "total_vendas": total_vendas,
        "caixas_abertos": caixas_abertos,
        "total_taxa_servico": total_taxa_servico,
    }
    return render(request, "financeiro/financeiro_caixa.html", context)
