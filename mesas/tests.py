from django.test import TestCase
from mesas.models import Mesa


class MesaModelTest(TestCase):
    def test_criacao_mesa(self):
        """Valida a criação de uma mesa e seu status inicial."""
        mesa = Mesa.objects.create(
            numero=5,
            status="livre",  # Removido o argumento 'capacidade' que causou o erro
        )
        self.assertEqual(mesa.numero, 5)
        self.assertEqual(mesa.status, "livre")
