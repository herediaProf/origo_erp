from django.db import models
from fornecedores.models import Fornecedor
from funcionarios.models import Funcionario


class EstoqueItem(models.Model):
    nome = models.CharField(max_length=255)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    responsavel_compra = models.ForeignKey(
        Funcionario, on_delete=models.SET_NULL, null=True
    )
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    peso = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unidade = models.CharField(max_length=20)  # ex: kg, un, litros
    volume = models.CharField(max_length=50, null=True, blank=True)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
