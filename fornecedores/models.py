from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Razão Social / Nome")
    cnpj_cpf = models.CharField(max_length=20, unique=True, verbose_name="CNPJ/CPF")
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
