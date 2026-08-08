from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import render
from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


def listar_produtos(request):
    produtos = list(Produto.objects.values())
    return JsonResponse(produtos, safe=False)


def produtos_dashboard_view(request):
    """Renderiza a interface visual e amigável para Produtos & Estoque"""
    return render(request, "produtos/dashboard_produtos.html")
