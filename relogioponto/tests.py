from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rh.models import Funcionario
from .models import RegistroPonto


class RegistroPontoTests(APITestCase):
    def setUp(self):
        self.funcionario = Funcionario.objects.create(
            nome="Ana Maria", salario_base=3000.00, data_admissao="2026-01-01"
        )
        self.url = reverse("registroponto-list")

    def test_registrar_ponto(self):
        data = {
            "funcionario": self.funcionario.id,
            "tipo": "ENTRADA",
            "observacao": "Chegada no horário",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RegistroPonto.objects.count(), 1)
        self.assertEqual(RegistroPonto.objects.get().tipo, "ENTRADA")
