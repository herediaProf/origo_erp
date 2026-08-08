from django.core.management.base import BaseCommand
from decimal import Decimal
from mesas.models import Mesa
from rh.models import Funcionario
from fornecedores.models import Fornecedor
from produtos.models import Categoria, Produto
from clientes.models import Cliente


class Command(BaseCommand):
    help = "Popula o banco de dados com dados iniciais para testes"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populando banco de dados...")

        # 1. Criar 20 Mesas
        for i in range(1, 21):
            Mesa.objects.get_or_create(numero=i, defaults={"status": "LIVRE"})

        # 2. Criar Categoria e Produto inicial (com a descrição preenchida)
        cat, _ = Categoria.objects.get_or_create(nome="Bebidas")
        Produto.objects.get_or_create(
            nome="Cerveja 600ml",
            defaults={
                "descricao": "Cerveja gelada 600ml",
                "preco": Decimal("15.00"),
                "categoria": cat,
                "estoque_atual": 100,
                "disponivel": True,
            },
        )

        # 3. Criar Fornecedor inicial
        Fornecedor.objects.get_or_create(
            cnpj_cpf="00000000000100",
            defaults={"nome": "Distribuidora Central", "telefone": "11999999999"},
        )

        # 4. Criar Cliente inicial
        Cliente.objects.get_or_create(
            cpf_cnpj="11122233344",
            defaults={"nome": "Cliente Padrão", "telefone": "11988888888"},
        )

        self.stdout.write(self.style.SUCCESS("Banco populado com sucesso!"))
