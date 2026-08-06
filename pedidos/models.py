import uuid
from django.db import models
from core.models import CustomUser
from produtos.models import Produto


class Mesa(models.Model):
    STATUS_MESA = (
        ("livre", "Livre"),
        ("ocupada", "Ocupada"),
        ("reservada", "Reservada"),
    )

    numero = models.IntegerField(unique=True)
    capacidade = models.IntegerField(default=4)
    status = models.CharField(max_length=20, choices=STATUS_MESA, default="livre")
    token_qrcode = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Mesa {self.numero} ({self.get_status_display()})"


class Pedido(models.Model):
    STATUS_PEDIDO = (
        ("aberto", "Aberto / Na Mesa"),
        ("enviado", "Enviado à Cozinha"),
        ("pronto", "Pronto para Entrega"),
        ("entregue", "Entregue"),
        ("fechado", "Fechado / Conta Paga"),
    )

    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name="pedidos")
    garcom = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": "garcom"},
        related_name="pedidos",
    )
    status = models.CharField(max_length=20, choices=STATUS_PEDIDO, default="aberto")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido #{self.id} - Mesa {self.mesa.numero}"

    @property
    def valor_total(self):
        return sum(item.subtotal for item in self.itens.all())


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Garante que o preço unitário seja congelado no momento do pedido
        if not self.preco_unitario:
            self.preco_unitario = self.produto.preco
        super().save(*args, **kwargs)

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Pedido #{self.pedido.id})"
