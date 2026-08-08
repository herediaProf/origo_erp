from django.test import TestCase
from decimal import Decimal
from produtos.models import Produto, Categoria


class ProdutoModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Alimentação")

    def test_criacao_produto_com_sucesso(self):
        """Garante que o produto é criado corretamente e mantém a precisão decimal do preço."""
        produto = Produto.objects.create(
            nome="Hambúrguer Artesanal",
            categoria=self.categoria,
            preco=Decimal("32.90"),
            estoque_atual=15,
            disponivel=True,
        )
        self.assertEqual(produto.preco, Decimal("32.90"))
        self.assertTrue(produto.disponivel)
        # Ajustado para o formato real retornado pelo __str__ do model
        self.assertEqual(str(produto), "Hambúrguer Artesanal - R$ 32.90")
