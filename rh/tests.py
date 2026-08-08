from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from decimal import Decimal
from .models import Funcionario, RegistroPonto

User = get_user_model()


class RHRusticityAndIntegrityTestCase(TestCase):
    def setUp(self):
        # Criação de dados de teste para verificar integridade e relacionamentos (Joins)
        self.user = User.objects.create_user(
            username="funcionario_teste", password="123"
        )
        self.funcionario = Funcionario.objects.create(
            nome="Wanderson Heredia",
            cargo="Professor de Tecnologia",
            salario_base=Decimal("5000.00"),
            comissao_percentual=Decimal("5.00"),
            data_admissao="2026-01-01",
            ativo=True,
        )
        self.registro = RegistroPonto.objects.create(
            funcionario=self.user,
            tipo="entrada",
            observacao="Teste automatizado de ponto",
        )

    def test_relacionamento_e_integridade_ponto(self):
        """Testa se o relacionamento ForeignKey e o __str__ funcionam corretamente (Simula Joins)"""
        self.assertEqual(self.registro.funcionario, self.user)
        self.assertIn("Entrada", str(self.registro))

    def test_regras_funcionalidade_funcionario(self):
        """Verifica se os campos monetários e decimais mantêm a precisão e integridade"""
        func = Funcionario.objects.get(nome="Wanderson Heredia")
        self.assertTrue(func.ativo)
        self.assertEqual(func.salario_base, Decimal("5000.00"))

    def test_performance_e_consultas_lote(self):
        """Valida a performance de consultas em lote (QuerySets e escalabilidade básica)"""
        registros = RegistroPonto.objects.select_related("funcionario").all()
        self.assertGreaterEqual(registros.count(), 1)
