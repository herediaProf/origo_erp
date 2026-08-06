from django.contrib import admin
from .models import Mesa, Pedido, ItemPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ("numero", "capacidade", "status", "token_qrcode")
    list_filter = ("status",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "mesa", "garcom", "status", "valor_total", "criado_em")
    list_filter = ("status", "criado_em")
    inlines = [ItemPedidoInline]
