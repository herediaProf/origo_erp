from django.contrib import admin
from .models import Venda, Caixa


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "data_venda" if hasattr(Venda, "data_venda") else "id",
        "forma_pagamento" if hasattr(Venda, "forma_pagamento") else "id",
    )
    search_fields = ("id",)


@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    list_display = ("id", "operador", "status", "data_abertura", "data_fechamento")
    list_filter = ("status", "data_abertura")
