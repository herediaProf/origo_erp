from django.contrib import admin
from .models import Cliente, Fornecedor, ItemPedido, Mesa, Pedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


class PedidoInline(admin.TabularInline):
    model = Pedido
    extra = 0
    show_change_link = True


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "telefone", "email"]
    search_fields = ["nome", "telefone"]


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "telefone", "email"]
    search_fields = ["nome"]


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ["numero", "capacidade", "status"]
    list_filter = ["status"]
    inlines = [PedidoInline]


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["id", "mesa", "cliente", "garcom", "status", "valor_total"]
    list_filter = ["status", "mesa", "garcom"]
    search_fields = ["id", "cliente__nome", "garcom__username"]
    inlines = [ItemPedidoInline]


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ["pedido", "produto", "quantidade", "preco_unitario", "subtotal"]
    list_filter = ["produto"]
