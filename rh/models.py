from django.db import models
from django.conf import settings
from django.utils import timezone


class RegistroPonto(models.Model):
    TIPO_REGISTRO = (
        ("entrada", "Entrada"),
        ("saida", "Saída"),
        ("pausa_inicio", "Início de Pausa"),
        ("pausa_fim", "Fim de Pausa"),
    )

    funcionario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="registros_ponto",
    )
    tipo = models.CharField(max_length=20, choices=TIPO_REGISTRO)
    data_hora = models.DateTimeField(default=timezone.now)
    observacao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Registro de Ponto"
        verbose_name_plural = "Registros de Ponto"
        ordering = ["-data_hora"]

    def __str__(self):
        return f"{self.funcionario.username} - {self.get_tipo_display()} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"


class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    comissao_percentual = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00
    )
    data_admissao = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.cargo}"
