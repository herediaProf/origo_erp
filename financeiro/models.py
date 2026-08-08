from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from pedidos.models import Pedido


class Caixa(models.Model):
    STATUS_CAIXA = [
        ("aberto", "Aberto"),
        ("fechado", "Fechado"),
    ]

    operador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CAIXA, default="aberto")
    saldo_inicial = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)]
    )
    saldo_final_dinheiro = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)]
    )
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-data_abertura"]

    def __str__(self):
        return f"Caixa #{self.id} - Operador: {self.operador} [{self.get_status_display()}]"


class Venda(models.Model):
    FORMAS_PAGAMENTO = [
        ("dinheiro", "Dinheiro"),
        ("cartao_credito", "Cartão de Crédito"),
        ("cartao_debito", "Cartão de Débito"),
        ("pix", "Pix"),
    ]

    pedido = models.OneToOneField(
        Pedido, on_delete=models.PROTECT, related_name="venda"
    )
    caixa = models.ForeignKey(Caixa, on_delete=models.PROTECT, related_name="vendas")
    forma_pagamento = models.CharField(max_length=30, choices=FORMAS_PAGAMENTO)
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    paga_taxa_servico = models.BooleanField(default=True)
    valor_taxa_servico = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)]
    )
    valor_total = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    data_venda = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data_venda"]

    def __str__(self):
        return f"Venda #{self.id} (Pedido #{self.pedido.id}) - R$ {self.valor_total}"


class RateioCaixinha(models.Model):
    caixa = models.OneToOneField(Caixa, on_delete=models.CASCADE, related_name="rateio")
    valor_total_caixinha = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    total_funcionarios_ativos = models.IntegerField(validators=[MinValueValidator(1)])
    valor_por_funcionario = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    data_rateio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rateio Caixa #{self.caixa.id} - R$ {self.valor_por_funcionario}/func"
