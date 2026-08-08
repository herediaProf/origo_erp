from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db import transaction
from .models import ItemPedido, Pedido

# Importação segura do app financeiro (caso já exista)
try:
    from financeiro.models import Transacao
except ImportError:
    Transacao = None


@receiver(post_save, sender=ItemPedido)
def gerenciar_item_pedido_salvo(sender, instance, created, **kwargs):
    pedido = instance.pedido

    # 1. Recalcula e atualiza automaticamente o valor total do pedido
    total_calculado = sum(item.subtotal for item in pedido.itens.all())
    if pedido.valor_total != total_calculado:
        pedido.valor_total = total_calculado
        pedido.save(update_fields=["valor_total"])

    # 2. Baixa no estoque com segurança (apenas na criação do item)
    if created:
        with transaction.atomic():
            produto = instance.produto
            produto_locked = produto.__class__.objects.select_for_update().get(
                pk=produto.pk
            )

            if produto_locked.estoque_atual >= instance.quantidade:
                produto_locked.estoque_atual -= instance.quantidade
                produto_locked.save(update_fields=["estoque_atual"])
            else:
                raise ValueError(f"Estoque insuficiente para o produto: {produto.nome}")


@receiver(pre_delete, sender=ItemPedido)
def devolver_estoque_ao_deletar_item(sender, instance, **kwargs):
    # Devolve o estoque caso o item seja removido do pedido
    with transaction.atomic():
        produto = instance.produto
        produto_locked = produto.__class__.objects.select_for_update().get(
            pk=produto.pk
        )

        produto_locked.estoque_atual += instance.quantidade
        produto_locked.save(update_fields=["estoque_atual"])


@receiver(post_save, sender=Pedido)
def integrar_pedido_ao_financeiro(sender, instance, created, **kwargs):
    # Se o pedido for concluído, lança a receita no Financeiro automaticamente
    if instance.status == "concluido" and Transacao:
        descricao_transacao = f"Pedido #{instance.id} - Mesa {instance.mesa.numero if instance.mesa else 'Balcão'}"

        # Evita duplicidade
        transacao_existe = Transacao.objects.filter(
            descricao=descricao_transacao
        ).exists()

        if not transacao_existe:
            Transacao.objects.create(
                descricao=descricao_transacao,
                valor=instance.valor_total,
                tipo="receita",
                status="pago",
            )
