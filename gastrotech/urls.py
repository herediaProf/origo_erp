from django.contrib import admin
from django.urls import path, include
from core.views import (
    dashboard_view,
    equipe_rh_view,
    financeiro_caixa_view,
    estoque_view,
    fornecedores_view,
    clientes_view,
    relogioponto_view,
)
from mesas.views import mesas_dashboard_view
from pedidos.views import pedidos_dashboard_view
from financeiro.views import financeiro_dashboard_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", dashboard_view, name="dashboard"),
    # Telas Visuais do ERP
    path("equipe-rh/", equipe_rh_view, name="equipe_rh"),
    path("financeiro-caixa/", financeiro_dashboard_view, name="financeiro_dashboard"),
    path("mesas/", mesas_dashboard_view, name="mesas_dashboard"),
    path("vendas-pedidos/", pedidos_dashboard_view, name="pedidos_dashboard"),
    path("estoque/itens/", estoque_view, name="estoque_view"),
    path("fornecedores/", fornecedores_view, name="fornecedores_view"),
    path("clientes/", clientes_view, name="clientes_view"),
    path("relogioponto/", relogioponto_view, name="relogioponto_view"),
    # APIs dos Apps (Sem duplicações)
    path("api/produtos/", include("produtos.urls")),
    path("api/pedidos/", include("pedidos.urls")),
    path("api/mesas/", include("mesas.urls")),
    path("api/financeiro/", include("financeiro.urls")),
    path("api/rh/", include("rh.urls")),
    path("api/estoque/", include("estoque.urls")),
    path("api/fornecedores/", include("fornecedores.urls")),
    path("api/clientes/", include("clientes.urls")),
    path("api/relogioponto/", include("relogioponto.urls")),
    path("api/compras/", include("compras.urls")),
    path("api/funcionarios/", include("funcionarios.urls")),
]
