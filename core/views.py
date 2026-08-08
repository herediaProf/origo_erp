from django.shortcuts import render, get_object_or_404, redirect
from clientes.models import Cliente
from funcionarios.models import Funcionario


def dashboard_view(request):
    return render(request, "core/dashboard.html")


def equipe_rh_view(request):
    return render(request, "core/equipe_rh.html")


def financeiro_caixa_view(request):
    return render(request, "core/financeiro_caixa.html")


# --- Módulos Criados ---


def estoque_view(request):
    return render(request, "estoque/index.html")


def fornecedores_view(request):
    return render(request, "fornecedores/index.html")


def clientes_view(request):
    """Renderiza a listagem visual de clientes buscados do banco de dados."""
    clientes = Cliente.objects.all()
    return render(request, "clientes/lista_clientes.html", {"clientes": clientes})


def funcionarios_view(request):
    """Renderiza a listagem visual de funcionários buscados do banco de dados."""
    funcionarios = Funcionario.objects.all()
    return render(
        request, "funcionarios/lista_funcionarios.html", {"funcionarios": funcionarios}
    )


def relogioponto_view(request):
    """Renderiza a interface visual do relógio de ponto."""
    return render(request, "relogioponto/ponto.html")
