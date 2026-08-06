from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Tipos de usuário definidos pelo seu requisito
    ROLE_CHOICES = (
        ("admin", "Administrador"),
        ("caixa", "Caixa"),
        ("garcom", "Garçom"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="garcom")
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
