from django.db import models
from fornecedores.models import Fornecedor
from funcionarios.models import Funcionario


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class EstoqueItem(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="itens",
    )
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.SET_NULL, null=True, blank=True
    )
    responsavel_compra = models.ForeignKey(
        Funcionario, on_delete=models.SET_NULL, null=True, blank=True
    )

    # Quantidades e Unidades
    quantidade = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )  # Saldo atual
    peso = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unidade = models.CharField(max_length=20, default="un")  # ex: kg, un, litros
    volume = models.CharField(max_length=50, null=True, blank=True)

    # Preços solicitados
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_atacado = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )  # Novo preço de atacado

    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} (Estoque: {self.quantidade} {self.unidade})"


class MovimentacaoEstoque(models.Model):
    """Controla as entradas e saídas de mercadorias do estoque de forma automatizada."""

    TIPO_CHOICES = (
        ("entrada", "Entrada de Mercadoria"),
        ("saida", "Saída de Mercadoria"),
    )

    item = models.ForeignKey(
        EstoqueItem, on_delete=models.CASCADE, related_name="movimentacoes"
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    responsavel = models.ForeignKey(
        Funcionario, on_delete=models.SET_NULL, null=True, blank=True
    )
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Atualiza o saldo do EstoqueItem automaticamente ao criar a movimentação
        if self.pk is None:
            if self.tipo == "entrada":
                self.item.quantidade += self.quantidade
            elif self.tipo == "saida":
                self.item.quantidade -= self.quantidade
            self.item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo.upper()} - {self.item.nome} ({self.quantidade})"
