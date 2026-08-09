from django.shortcuts import render
from clientes.models import Cliente
from funcionarios.models import Funcionario


def dashboard_view(request):
    """Renderiza o dashboard principal do ERP."""
    return render(request, "core/dashboard.html")


def equipe_rh_view(request):
    """Renderiza a página da equipe de RH."""
    return render(request, "core/equipe_rh.html")


# --- Módulos Visuais do ERP ---


def estoque_view(request):
    """Renderiza a página inicial do módulo de estoque."""
    return render(request, "estoque/index.html")


def fornecedores_view(request):
    """Renderiza a página inicial do módulo de fornecedores."""
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
