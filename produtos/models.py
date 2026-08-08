from django.db import models
from django.core.validators import MinValueValidator


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="produtos"
    )
    estoque_atual = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(preco__gte=0), name="preco_nao_negativo"
            ),
            models.CheckConstraint(
                condition=models.Q(estoque_atual__gte=0), name="estoque_nao_negativo"
            ),
        ]
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"
