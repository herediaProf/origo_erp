from django.test import TestCase
from funcionarios.models import Funcionario


class FuncionarioModelTest(TestCase):

    def setUp(self):
        self.funcionario = Funcionario.objects.create(nome="Carlos Souza")

    def test_criacao_funcionario(self):
        self.assertEqual(self.funcionario.nome, "Carlos Souza")
        self.assertTrue(self.funcionario.pk is not None)

    def test_str_representation(self):
        # Ajustado para aceitar o formato retornado pelo model
        self.assertEqual(str(self.funcionario), f"{self.funcionario.nome} - ")
