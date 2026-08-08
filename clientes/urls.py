from django.urls import path
from clientes.views import clientes_view, salvar_cliente, deletar_cliente

app_name = "clientes"

urlpatterns = [
    path("", clientes_view, name="lista_clientes"),
    path("novo/", salvar_cliente, name="novo_cliente"),
    path("editar/<int:pk>/", salvar_cliente, name="editar_cliente"),
    path("deletar/<int:pk>/", deletar_cliente, name="deletar_cliente"),
]
