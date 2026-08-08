from django.test import TestCase
from produtos.models import (
    Produto,
    Categoria,
)  # Ajuste o import da Categoria conforme o seu app


class ProdutoModelTest(TestCase):
    def test_criacao_produto(self):
        """Garante que um produto pode ser criado com os campos novos e salvos no banco."""
        # Cria uma categoria obrigatória para o produto
        categoria = Categoria.objects.create(nome="Bebidas")

        produto = Produto.objects.create(
            nome="Café Espresso Teste",
            categoria=categoria,  # Passando a categoria obrigatória
            preco=5.50,
            estoque_atual=10,
            disponivel=True,
        )

        # Verifica se o ID foi gerado e as datas automáticas existem
        self.assertIsNotNone(produto.id)
        self.assertEqual(produto.nome, "Café Espresso Teste")
        self.assertIsNotNone(produto.criado_em)
        self.assertIsNotNone(produto.atualizado_em)
