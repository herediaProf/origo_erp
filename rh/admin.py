from django.contrib import admin
from .models import (
    Funcionario,
    RegistroPonto,
)  # Ajuste os imports conforme os seus models


# Registra o modelo Funcionario para que ele apareça no Django Admin
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "cargo",
        "ativo",
    )  # Campos que deseja exibir na listagem
    search_fields = ("nome", "cargo")


@admin.register(RegistroPonto)
class RegistroPontoAdmin(admin.ModelAdmin):
    list_display = ("funcionario", "tipo", "data_hora", "observacao")
    list_filter = ("tipo", "data_hora")
