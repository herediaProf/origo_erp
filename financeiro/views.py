from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from rest_framework import viewsets
from .models import Caixa, Venda, RateioCaixinha
from .serializers import (
    CaixaSerializer,
    VendaSerializer,
    RateioCaixinhaSerializer,
)
from pedidos.models import Pedido


# ==========================================
# APIs (Django REST Framework)
# ==========================================
class CaixaViewSet(viewsets.ModelViewSet):
    queryset = Caixa.objects.select_related("operador").prefetch_related("vendas").all()
    serializer_class = CaixaSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.select_related("pedido", "caixa").all()
    serializer_class = VendaSerializer


class RateioCaixinhaViewSet(viewsets.ModelViewSet):
    queryset = RateioCaixinha.objects.select_related("caixa").all()
    serializer_class = RateioCaixinhaSerializer


# ==========================================
# VIEWS VISUAIS (Telas HTML do Sistema)
# ==========================================


@login_required
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


# --- GESTÃO DE CAIXAS (Visual) ---
@login_required
def lista_caixas_view(request):
    """Lista todos os caixas abertos e fechados."""
    caixas = Caixa.objects.select_related("operador").all().order_by("-id")
    return render(request, "financeiro/lista_caixas.html", {"caixas": caixas})


@login_required
def abrir_caixa_view(request):
    """Abre um novo caixa vinculado ao operador autenticado."""
    # Verifica se já existe um caixa aberto para evitar duplicidade incorreta
    caixa_aberto = Caixa.objects.filter(status="aberto").first()

    if request.method == "POST":
        if caixa_aberto:
            return redirect("/api/financeiro/vendas-view/novo/")

        saldo_inicial = request.POST.get("saldo_inicial") or "0.00"

        # Usa o usuário autenticado da requisição como operador
        Caixa.objects.create(
            operador=request.user, saldo_inicial=saldo_inicial, status="aberto"
        )
        return redirect("/api/financeiro/vendas-view/novo/")

    return render(
        request,
        "financeiro/abrir_caixa.html",
        {"caixa_aberto": caixa_aberto, "titulo": "Abrir Novo Caixa"},
    )


@login_required
def fechar_caixa_view(request, pk):
    """Fecha um caixa existente registrando o saldo final e a data de fechamento."""
    caixa = get_object_or_404(Caixa, pk=pk, status="aberto")

    if request.method == "POST":
        saldo_final_dinheiro = request.POST.get("saldo_final_dinheiro") or "0.00"

        caixa.saldo_final_dinheiro = saldo_final_dinheiro
        caixa.data_fechamento = timezone.now()
        caixa.status = "fechado"
        caixa.save()

        return redirect("/api/financeiro/caixas-view/")

    return render(request, "financeiro/fechar_caixa.html", {"caixa": caixa})


# --- GESTÃO DE VENDAS (Visual) ---
@login_required
def lista_vendas_view(request):
    """Lista todas as vendas realizadas."""
    vendas = Venda.objects.select_related("pedido", "caixa").all().order_by("-id")
    return render(request, "financeiro/lista_vendas.html", {"vendas": vendas})


@login_required
def salvar_venda_view(request, pk=None):
    """Registra ou edita uma venda vinculando-a obrigatoriamente a um caixa aberto."""
    venda_obj = get_object_or_404(Venda, pk=pk) if pk else None

    # Validação rigorosa: Não é possível vender sem um caixa aberto
    caixa_ativo = Caixa.objects.filter(status="aberto").first()
    if not caixa_ativo and not venda_obj:
        return redirect("/api/financeiro/caixas-view/abrir/")

    if request.method == "POST":
        pedido_id = request.POST.get("pedido_id")

        # Validação: Garante que um pedido foi selecionado no formulário
        if not pedido_id:
            pedidos_disponiveis = Pedido.objects.all()
            context = {
                "venda": venda_obj,
                "caixa_ativo": caixa_ativo,
                "pedidos": pedidos_disponiveis,
                "erro": "Você precisa selecionar um pedido válido para registrar a venda.",
            }
            return render(request, "financeiro/form_venda.html", context)

        forma_pagamento = request.POST.get("forma_pagamento", "dinheiro")
        subtotal = request.POST.get("subtotal") or "0.00"
        paga_taxa_servico = (
            True if request.POST.get("paga_taxa_servico") == "on" else False
        )
        valor_taxa_servico = request.POST.get("valor_taxa_servico") or "0.00"
        valor_total = request.POST.get("valor_total") or subtotal

        pedido_obj = get_object_or_404(Pedido, pk=pedido_id)

        if venda_obj:
            # Edição de venda existente
            venda_obj.pedido = pedido_obj
            venda_obj.forma_pagamento = forma_pagamento
            venda_obj.subtotal = subtotal
            venda_obj.paga_taxa_servico = paga_taxa_servico
            venda_obj.valor_taxa_servico = valor_taxa_servico
            venda_obj.valor_total = valor_total
            venda_obj.save()
        else:
            # Criação de nova venda usando o caixa ativo do sistema
            Venda.objects.create(
                pedido=pedido_obj,
                caixa=caixa_ativo,
                forma_pagamento=forma_pagamento,
                subtotal=subtotal,
                paga_taxa_servico=paga_taxa_servico,
                valor_taxa_servico=valor_taxa_servico,
                valor_total=valor_total,
            )

        return redirect("/api/financeiro/vendas-view/")

    pedidos_disponiveis = Pedido.objects.all()
    context = {
        "venda": venda_obj,
        "caixa_ativo": caixa_ativo,
        "pedidos": pedidos_disponiveis,
    }
    return render(request, "financeiro/form_venda.html", context)


@login_required
def deletar_venda_view(request, pk):
    """Exclui uma venda."""
    venda = get_object_or_404(Venda, pk=pk)
    venda.delete()
    return redirect("/api/financeiro/vendas-view/")
