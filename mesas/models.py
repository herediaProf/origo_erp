import uuid
from django.db import models


class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    status = models.CharField(max_length=50, default="livre")
    token_qrcode = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return f"Mesa {self.numero}"
