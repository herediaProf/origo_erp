from django.test import TestCase
from clientes.models import Cliente


class ClienteModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="Maria da Silva",
            cpf_cnpj="12345678901",
            telefone="11988887777",
            email="maria@email.com",
        )

    def test_criacao_cliente(self):
        """Garante que o cliente foi criado corretamente no banco."""
        self.assertEqual(self.cliente.nome, "Maria da Silva")
        self.assertEqual(self.cliente.cpf_cnpj, "12345678901")
        self.assertTrue(self.cliente.pk is not None)

    def test_str_representation(self):
        """Verifica se o método __str__ retorna o nome esperado."""
        self.assertEqual(str(self.cliente), self.cliente.nome)
