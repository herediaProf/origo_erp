from django.db import models
from produtos.models import Produto
from rh.models import Funcionario


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    capacidade = models.IntegerField(default=4)
    status = models.CharField(max_length=50, default="Livre")
    token_qrcode = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Mesa {self.numero}"


class Pedido(models.Model):
    STATUS_CHOICES = [
        ("aberto", "Aberto"),
        ("preparacao", "Em Preparação"),
        ("concluido", "Concluído"),
        ("cancelado", "Cancelado"),
    ]

    cliente = models.ForeignKey(
        Cliente, on_delete=models.SET_NULL, null=True, blank=True
    )
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="aberto")
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    garcom = models.ForeignKey(
        Funcionario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pedidos",
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido #{self.id} - Mesa {self.mesa.numero if self.mesa else 'Balcão'}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    observacao = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calcula automaticamente o subtotal do item ao salvar
        self.subtotal = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Pedido #{self.pedido.id})"
