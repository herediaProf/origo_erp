from django.db import models
from django.utils import timezone  # Importe o timezone aqui
from rh.models import Funcionario


class RegistroPonto(models.Model):
    TIPO_REGISTRO = [
        ("ENTRADA", "Entrada"),
        ("SAIDA_ALMOCO", "Saída Almoço"),
        ("RETORNO_ALMOCO", "Retorno Almoço"),
        ("SAIDA", "Saída"),
    ]

    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.CASCADE, related_name="registros_ponto"
    )
    data_hora = models.DateTimeField(
        default=timezone.now
    )  # Usando default para evitar o prompt
    tipo = models.CharField(
        max_length=20, choices=TIPO_REGISTRO, default="ENTRADA"
    )  # Definindo um default temporário
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-data_hora"]

    def __str__(self):
        return f"{self.funcionario.nome} - {self.tipo} em {self.data_hora}"
