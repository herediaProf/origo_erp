from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from fornecedores.models import Fornecedor
from funcionarios.models import Funcionario
from .models import EstoqueItem


class EstoqueItemTests(APITestCase):
    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste", cnpj_cpf="12345678000199"
        )
        self.funcionario = Funcionario.objects.create(nome="Carlos Teste")
        self.url = reverse("estoqueitem-list")

    def criar_item(self):
        return EstoqueItem.objects.create(
            nome="Tomate",
            fornecedor=self.fornecedor,
            responsavel_compra=self.funcionario,
            quantidade=50.00,
            unidade="kg",
            valor_compra=5.00,
            valor_venda=10.00,
        )

    def test_listar_itens_estoque(self):
        self.criar_item()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_criar_item_estoque(self):
        data = {
            "nome": "Cebola",
            "fornecedor": self.fornecedor.id,
            "responsavel_compra": self.funcionario.id,
            "quantidade": 30.00,
            "unidade": "kg",
            "valor_compra": 4.00,
            "valor_venda": 8.00,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EstoqueItem.objects.count(), 1)
