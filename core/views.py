from django.shortcuts import render


def dashboard_view(request):
    return render(request, "core/dashboard.html")


def equipe_rh_view(request):
    return render(request, "core/equipe_rh.html")


def financeiro_caixa_view(request):
    return render(request, "core/financeiro_caixa.html")


# --- Novas Views para os módulos criados ---


def estoque_view(request):
    return render(request, "estoque/index.html")


def fornecedores_view(request):
    return render(request, "fornecedores/index.html")


def clientes_view(request):
    return render(request, "clientes/index.html")


def relogioponto_view(request):
    return render(request, "relogioponto/index.html")
