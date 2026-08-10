from django.db import models
from django.utils import timezone
from rh.models import Funcionario


class RegistroPonto(models.Model):
    # Organizado com nomes mais claros e inclusão da Hora Extra
    TIPO_REGISTRO = [
        ("ENTRADA", "Entrada"),
        ("SAIDA_ALMOCO", "Saída Almoço"),
        ("RETORNO_ALMOCO", "Retorno Almoço"),
        ("SAIDA", "Saída"),
        ("HORA_EXTRA", "Hora Extra"),
    ]

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE,
        related_name="registros_ponto",
        verbose_name="Funcionário",
    )

    data_hora = models.DateTimeField(default=timezone.now, verbose_name="Data e Hora")

    tipo = models.CharField(
        max_length=20, choices=TIPO_REGISTRO, verbose_name="Tipo de Registro"
    )

    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    class Meta:
        verbose_name = "Registro de Ponto"
        verbose_name_plural = "Registros de Ponto"
        ordering = ["-data_hora"]

    def __str__(self):
        # Formatando a data para ficar mais legível no admin/logs
        data_formatada = self.data_hora.strftime("%d/%m/%Y %H:%M")
        return f"{self.funcionario.nome} | {self.get_tipo_display()} | {data_formatada}"
