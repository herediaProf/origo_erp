from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CaixaViewSet,
    VendaViewSet,
    RateioCaixinhaViewSet,
    financeiro_dashboard_view,
    # Novas views visuais importadas:
    lista_caixas_view,
    abrir_caixa_view,
    fechar_caixa_view,
    lista_vendas_view,
    salvar_venda_view,
    deletar_venda_view,
)

# Router para as APIs do DRF
router = DefaultRouter()
router.register(r"caixas", CaixaViewSet)
router.register(r"vendas", VendaViewSet)
router.register(r"rateios", RateioCaixinhaViewSet)

urlpatterns = [
    # Dashboard principal do financeiro
    path("dashboard/", financeiro_dashboard_view, name="financeiro_dashboard"),
    # --- Rotas Visuais (Telas HTML) ---
    # Caixas
    path("caixas-view/", lista_caixas_view, name="lista_caixas_view"),
    path("caixas-view/abrir/", abrir_caixa_view, name="abrir_caixa_view"),
    path("caixas-view/fechar/<int:pk>/", fechar_caixa_view, name="fechar_caixa_view"),
    # Vendas
    path("vendas-view/", lista_vendas_view, name="lista_vendas_view"),
    path("vendas-view/novo/", salvar_venda_view, name="nova_venda_view"),
    path("vendas-view/editar/<int:pk>/", salvar_venda_view, name="editar_venda_view"),
    path(
        "vendas-view/deletar/<int:pk>/", deletar_venda_view, name="deletar_venda_view"
    ),
    # APIs do Django REST Framework (mantidas intactas)
    path("", include(router.urls)),
]
