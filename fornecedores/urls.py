from django.urls import path
from .views import (
    lista_fornecedores_view,
    salvar_fornecedor_view,
    deletar_fornecedor_view,
)

urlpatterns = [
    path("", lista_fornecedores_view, name="fornecedores_lista"),
    path("novo/", salvar_fornecedor_view, name="fornecedor_novo"),
    path("editar/<int:pk>/", salvar_fornecedor_view, name="fornecedor_editar"),
    path("deletar/<int:pk>/", deletar_fornecedor_view, name="fornecedor_deletar"),
]
