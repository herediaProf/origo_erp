from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from fornecedores.models import Fornecedor
from funcionarios.models import Funcionario
from .models import EstoqueItem

User = get_user_model()


class EstoqueItemTests(TestCase):
    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste", cnpj_cpf="12345678000199"
        )
        self.funcionario = Funcionario.objects.create(nome="Carlos Teste")

    def test_criar_item_estoque(self):
        """Valida se o item de estoque é criado corretamente com os valores exatos."""
        item = EstoqueItem.objects.create(
            nome="Cebola",
            fornecedor=self.fornecedor,
            responsavel_compra=self.funcionario,
            quantidade=Decimal("30.00"),
            unidade="kg",
            valor_compra=Decimal("4.00"),
            valor_venda=Decimal("8.00"),
        )
        self.assertEqual(EstoqueItem.objects.count(), 1)
        self.assertEqual(item.nome, "Cebola")
        self.assertEqual(item.quantidade, Decimal("30.00"))

    def test_listar_itens_estoque(self):
        """Valida a listagem de itens salvos no banco de dados."""
        EstoqueItem.objects.create(
            nome="Tomate",
            fornecedor=self.fornecedor,
            responsavel_compra=self.funcionario,
            quantidade=Decimal("50.00"),
            unidade="kg",
            valor_compra=Decimal("5.00"),
            valor_venda=Decimal("10.00"),
        )
        itens = EstoqueItem.objects.all()
        self.assertEqual(itens.count(), 1)
        self.assertEqual(itens[0].nome, "Tomate")
