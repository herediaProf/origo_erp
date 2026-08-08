# orgo_erp/pedidos/services.py
from django.db import transaction
from django.core.exceptions import ValidationError


def processar_baixa_estoque(pedido):
    with transaction.atomic():
        for (
            item
        ) in pedido.itens.all():  # Certifique-se que o related_name='itens' existe
            produto = item.produto
            if produto.estoque_atual < item.quantidade:
                raise ValidationError(
                    f"Estoque insuficiente para o produto: {produto.nome}"
                )

            produto.estoque_atual -= item.quantidade
            produto.save()
