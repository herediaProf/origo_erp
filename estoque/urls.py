from django.urls import path
from .views import lista_estoque_view, salvar_produto_view, deletar_produto_view

app_name = "estoque"

urlpatterns = [
    path("", lista_estoque_view, name="estoque_lista"),
    path("novo/", salvar_produto_view, name="produto_novo"),
    path("editar/<int:pk>/", salvar_produto_view, name="editar_produto"),
    path("deletar/<int:pk>/", deletar_produto_view, name="excluir_produto"),
]
