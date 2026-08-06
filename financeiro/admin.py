from django.contrib import admin
from .models import Caixa, Venda, RateioCaixinha


class VendaInline(admin.TabularInline):
    model = Venda
    extra = 0
    readonly_fields = ("subtotal", "valor_taxa_servico", "valor_total", "data_venda")


@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "operador",
        "status",
        "saldo_inicial",
        "saldo_final_dinheiro",
        "data_abertura",
        "data_fechamento",
    )
    list_filter = ("status", "data_abertura")
    inlines = [VendaInline]


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pedido",
        "caixa",
        "forma_pagamento",
        "subtotal",
        "valor_taxa_servico",
        "valor_total",
        "data_venda",
    )
    list_filter = ("forma_pagamento", "paga_taxa_servico", "data_venda")


@admin.register(RateioCaixinha)
class RateioCaixinhaAdmin(admin.ModelAdmin):
    list_display = (
        "caixa",
        "valor_total_caixinha",
        "total_funcionarios_ativos",
        "valor_por_funcionario",
        "data_rateio",
    )
    readonly_fields = (
        "caixa",
        "valor_total_caixinha",
        "total_funcionarios_ativos",
        "valor_por_funcionario",
        "data_rateio",
    )
