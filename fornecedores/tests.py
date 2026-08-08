from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Fornecedor


class FornecedorTests(APITestCase):
    def setUp(self):
        self.url = reverse("fornecedor-list")

    def test_criar_fornecedor(self):
        data = {
            "nome": "Distribuidora Alimentos LTDA",
            "cnpj_cpf": "99888777000155",
            "telefone": "11999998888",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Fornecedor.objects.count(), 1)
        self.assertEqual(Fornecedor.objects.get().nome, "Distribuidora Alimentos LTDA")
