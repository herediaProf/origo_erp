from decimal import Decimal
from django.db import models
from django.conf import settings
from django.utils import timezone
from pedidos.models import Pedido


class Caixa(models.Model):
    STATUS_CHOICES = (
        ("aberto", "Aberto"),
        ("fechado", "Fechado"),
    )

    operador = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="caixas"
    )
    saldo_inicial = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00")
    )
    saldo_final_dinheiro = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="aberto")
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Caixa #{self.id} - Operador: {self.operador.username} ({self.get_status_display()})"

    def fechar_caixa(self, saldo_dinheiro_informado):
        """Fecha o caixa e calcula automaticamente o rateio da caixinha (10%)."""
        self.saldo_final_dinheiro = saldo_dinheiro_informado
        self.status = "fechado"
        self.data_fechamento = timezone.now()
        self.save()

        # Executa o rateio dos 10% acumulados neste caixa
        self.calcular_rateio_caixinha()

    def calcular_rateio_caixinha(self):
        from core.models import CustomUser

        # Soma todas as taxas de serviço (10%) das vendas deste caixa
        total_caixinha = self.vendas.filter(paga_taxa_servico=True).aggregate(
            total=models.Sum("valor_taxa_servico")
        )["total"] or Decimal("0.00")

        # Busca todos os funcionários ativos no sistema
        funcionarios_ativos = CustomUser.objects.filter(is_active=True).count()

        if funcionarios_ativos > 0 and total_caixinha > Decimal("0.00"):
            valor_por_pessoa = total_caixinha / Decimal(funcionarios_ativos)

            RateioCaixinha.objects.create(
                caixa=self,
                valor_total_caixinha=total_caixinha,
                total_funcionarios_ativos=funcionarios_ativos,
                valor_por_funcionario=valor_por_pessoa,
            )


class Venda(models.Model):
    FORMA_PAGAMENTO = (
        ("dinheiro", "Dinheiro"),
        ("pix", "PIX"),
        ("cartao_credito", "Cartão de Crédito"),
        ("cartao_debito", "Cartão de Débito"),
    )

    caixa = models.ForeignKey(Caixa, on_delete=models.PROTECT, related_name="vendas")
    pedido = models.OneToOneField(
        Pedido, on_delete=models.PROTECT, related_name="venda"
    )
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    paga_taxa_servico = models.BooleanField(
        default=True, verbose_name="Inclui 10% da Caixinha?"
    )
    valor_taxa_servico = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00")
    )
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    data_venda = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # 1. Puxa o valor total dos itens do pedido
        self.subtotal = self.pedido.valor_total

        # 2. Calcula 10% de caixinha se aceito pelo cliente
        if self.paga_taxa_servico:
            self.valor_taxa_servico = self.subtotal * Decimal("0.10")
        else:
            self.valor_taxa_servico = Decimal("0.00")

        # 3. Define o valor final cobrado
        self.valor_total = self.subtotal + self.valor_taxa_servico

        # 4. Atualiza o status do pedido para 'fechado'
        self.pedido.status = "fechado"
        self.pedido.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venda #{self.id} - Pedido #{self.pedido.id} (Total: R$ {self.valor_total})"


class RateioCaixinha(models.Model):
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE, related_name="rateios")
    valor_total_caixinha = models.DecimalField(max_digits=10, decimal_places=2)
    total_funcionarios_ativos = models.PositiveIntegerField()
    valor_por_funcionario = models.DecimalField(max_digits=10, decimal_places=2)
    data_rateio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rateio Caixa #{self.caixa.id}: R$ {self.valor_por_funcionario} / pessoa ({self.total_funcionarios_ativos} funcionários)"
