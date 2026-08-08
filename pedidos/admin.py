from django.contrib import admin
from .models import Mesa, Pedido, ItemPedido, Cliente, Fornecedor


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1
    readonly_fields = ["subtotal"]


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ["numero", "capacidade", "status", "token_qrcode"]
    list_filter = ["status"]
    search_fields = ["numero"]


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["id", "cliente", "mesa", "status", "valor_total", "criado_em"]
    list_filter = ["status", "criado_em"]
    search_fields = ["id", "cliente__nome"]
    inlines = [ItemPedidoInline]
    readonly_fields = ["valor_total", "criado_em", "atualizado_em"]


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome", "cpf_cnpj", "telefone", "email"]
    search_fields = ["nome", "cpf_cnpj"]


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ["nome", "cnpj", "telefone", "email"]
    search_fields = ["nome", "cnpj"]
