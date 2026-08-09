from django.test import TestCase
from decimal import Decimal
from compras.models import (
    Compra,
)  # Ajuste o nome do model se for PedidoCompra ou similar
from fornecedores.models import Fornecedor


class CompraModelTest(TestCase):

    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(
            nome="Atacadista Global", cnpj_cpf="11222333000199", telefone="11966665555"
        )
        # Criação de uma compra de exemplo (ajuste os campos conforme o seu model real)
        self.compra = Compra.objects.create(
            fornecedor=self.fornecedor,
            valor_total=Decimal("1500.50"),
            status="PENDENTE",
        )

    def test_criacao_compra(self):
        """Verifica se a compra está vinculada ao fornecedor correto e com o valor exato."""
        self.assertEqual(self.compra.fornecedor.nome, "Atacadista Global")
        self.assertEqual(self.compra.valor_total, Decimal("1500.50"))
        self.assertEqual(self.compra.status, "PENDENTE")
