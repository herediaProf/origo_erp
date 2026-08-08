from django.db import models
from fornecedores.models import Fornecedor
from funcionarios.models import Funcionario


class Compra(models.Model):
    STATUS_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("APROVADA", "Aprovada"),
        ("CONCLUIDA", "Concluída"),
        ("CANCELADA", "Cancelada"),
    ]

    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.PROTECT, related_name="compras"
    )
    comprador = models.ForeignKey(
        Funcionario,
        on_delete=models.SET_NULL,
        null=True,
        related_name="compras_realizadas",
    )
    data_compra = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDENTE")
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-data_compra"]

    def __str__(self):
        return f"Compra #{self.id} - {self.fornecedor.nome}"
