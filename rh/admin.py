from django.contrib import admin
from .models import Funcionario, RegistroPonto


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    # Substitua 'telefone' pelo nome real do campo no seu models.py (ex: 'celular', 'email')
    # ou remova-o da tupla se não existir.
    list_display = ("id", "nome", "cargo", "ativo")
    list_filter = ("cargo", "ativo")
    search_fields = ("nome", "cargo")
    ordering = ("nome",)


@admin.register(RegistroPonto)
class RegistroPontoAdmin(admin.ModelAdmin):
    list_display = ("id", "funcionario", "tipo", "data_hora")
    list_filter = ("tipo", "data_hora")
    search_fields = ("funcionario__nome",)
    date_hierarchy = "data_hora"
    ordering = ("-data_hora",)
