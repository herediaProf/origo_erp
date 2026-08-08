from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    funcao = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return f"{self.nome} - {self.funcao}"
