from django.test import TestCase
from fornecedores.models import Fornecedor


class FornecedorModelTest(TestCase):
    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste", cnpj_cpf="12345678000199", telefone="11999998888"
        )

    def test_criar_fornecedor(self):
        self.assertEqual(self.fornecedor.nome, "Fornecedor Teste")
        self.assertTrue(self.fornecedor.pk is not None)
