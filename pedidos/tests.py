from django.test import TestCase
from decimal import Decimal
from .models import Pedido


class PedidoModelTest(TestCase):
    def test_criacao_pedido_valida(self):
        """Valida a estrutura inicial de um pedido."""
        pedido = Pedido.objects.create(status="ABERTO", valor_total=Decimal("0.00"))
        self.assertTrue(Pedido.objects.filter(pk=pedido.pk).exists())
        self.assertEqual(pedido.status, "ABERTO")
        self.assertEqual(pedido.valor_total, Decimal("0.00"))
