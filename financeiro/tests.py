from django.test import TestCase
from decimal import Decimal
from django.contrib.auth import get_user_model
from mesas.models import Mesa
from pedidos.models import Pedido
from financeiro.models import Caixa, Venda

User = get_user_model()


class FinanceiroTestCase(TestCase):
    def setUp(self):
        # Criação de dados de apoio para os testes
        self.operador = User.objects.create_user(
            username="operador_caixa", password="123"
        )
        self.mesa = Mesa.objects.create(numero=1, status="OCUPADA")
        self.pedido = Pedido.objects.create(
            mesa=self.mesa, status="ABERTO", valor_total=Decimal("50.00")
        )

    def test_abertura_de_caixa(self):
        """Valida se o caixa é aberto corretamente com saldo inicial."""
        caixa = Caixa.objects.create(
            operador=self.operador, status="aberto", saldo_inicial=Decimal("150.00")
        )
        self.assertTrue(Caixa.objects.filter(pk=caixa.pk).exists())
        self.assertEqual(caixa.saldo_inicial, Decimal("150.00"))
        self.assertEqual(caixa.status, "aberto")

    def test_registro_de_venda(self):
        """Valida se uma venda é associada corretamente ao caixa e ao pedido."""
        caixa = Caixa.objects.create(
            operador=self.operador, status="aberto", saldo_inicial=Decimal("100.00")
        )

        venda = Venda.objects.create(
            pedido=self.pedido,
            caixa=caixa,
            forma_pagamento="dinheiro",
            subtotal=Decimal("50.00"),
            paga_taxa_servico=True,
            valor_taxa_servico=Decimal("5.00"),
            valor_total=Decimal("55.00"),
        )

        self.assertEqual(venda.valor_total, Decimal("55.00"))
        self.assertEqual(venda.caixa, caixa)
        self.assertEqual(venda.pedido, self.pedido)
        self.assertEqual(caixa.vendas.count(), 1)
