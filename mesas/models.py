from django.db import models


class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    status = models.CharField(max_length=50, default="Disponível")

    def __str__(self):
        return f"Mesa {self.numero}"
