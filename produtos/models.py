from django.core.validators import MinValueValidator
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Preço",
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="produtos",
        verbose_name="Categoria",
    )
    estoque_atual = models.IntegerField(
        default=0, validators=[MinValueValidator(0)], verbose_name="Estoque Atual"
    )
    disponivel = models.BooleanField(default=True, verbose_name="Disponível")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
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
