import random
from django.core.management.base import BaseCommand
from django.db import transaction

from produtos.models import Categoria, Produto
from pedidos.models import Cliente, Fornecedor, Mesa, Pedido, ItemPedido
from rh.models import RegistroPonto


class Command(BaseCommand):
    help = "Popula o banco de dados do ERP com massa de dados inicial (Mocks) de forma segura."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(
            self.style.WARNING("Iniciando o processo de mock do banco de dados...")
        )

        # 1. Criar ou Atualizar Categorias
        categorias_dados = [
            ("Bebidas", "Categoria de Bebidas"),
            ("Porções", "Categoria de Porções"),
            ("Pratos Principais", "Categoria de Pratos Principais"),
            ("Sobremesas", "Categoria de Sobremesas"),
            ("Insumos", "Categoria de Insumos"),
        ]
        categorias_map = {}
        for nome, desc in categorias_dados:
            cat, _ = Categoria.objects.update_or_create(
                nome=nome, defaults={"descricao": desc}
            )
            categorias_map[nome] = cat
        self.stdout.write(
            self.style.SUCCESS(f"{len(categorias_map)} categorias garantidas.")
        )

        # 2. Criar ou Atualizar Fornecedores
        fornecedores_dados = [
            (
                "Distribuidora de Bebidas Alvorada",
                "12.345.678/0001-90",
                "(12) 3892-1000",
            ),
            ("Atacadão de Carnes e Secos", "98.765.432/0001-12", "(12) 3893-2000"),
            ("Hortifrúti Campo Verde", "45.123.789/0001-55", "(12) 3894-3000"),
        ]
        fornecedores = []
        for nome, cnpj, tel in fornecedores_dados:
            forn, _ = Fornecedor.objects.update_or_create(
                cnpj=cnpj, defaults={"nome": nome, "telefone": tel}
            )
            fornecedores.append(forn)
        self.stdout.write(
            self.style.SUCCESS(f"{len(fornecedores)} fornecedores garantidos.")
        )

        # 3. Criar ou Atualizar Produtos (Incluindo a descrição obrigatória)
        produtos_dados = [
            (
                "Cerveja Pilsen 600ml",
                categorias_map["Bebidas"],
                12.00,
                50,
                "Cerveja puramalta 600ml gelada",
            ),
            (
                "Refrigerante Lata 350ml",
                categorias_map["Bebidas"],
                6.00,
                100,
                "Refrigerante em lata diversos sabores",
            ),
            (
                "Porção de Batata Frita",
                categorias_map["Porções"],
                35.00,
                30,
                "Porção tradicional com bacon e cheddar",
            ),
            (
                "Filé à Parmegiana",
                categorias_map["Pratos Principais"],
                65.00,
                20,
                "Acompanha arroz e fritas",
            ),
            (
                "Pudim de Leite Condensado",
                categorias_map["Sobremesas"],
                12.00,
                15,
                "Fatia tradicional de pudim caseiro",
            ),
        ]
        produtos = []
        for nome, cat, preco, estoque, descricao in produtos_dados:
            prod, _ = Produto.objects.update_or_create(
                nome=nome,
                defaults={
                    "categoria": cat,
                    "preco": preco,
                    "estoque_atual": estoque,
                    "descricao": descricao,
                    "disponivel": True,
                },
            )
            produtos.append(prod)
        self.stdout.write(
            self.style.SUCCESS(f"{len(produtos)} produtos cadastrados/verificados.")
        )

        # 4. Criar ou Atualizar Clientes
        clientes_dados = [
            ("Ana Souza", "111.222.333-44", "(12) 99111-2222"),
            ("Carlos Eduardo", "555.666.777-88", "(12) 99222-3333"),
            ("Mariana Lima", "999.888.777-66", "(12) 99333-4444"),
        ]
        clientes = []
        for nome, cpf, tel in clientes_dados:
            cli, _ = Cliente.objects.update_or_create(
                cpf_cnpj=cpf, defaults={"nome": nome, "telefone": tel}
            )
            clientes.append(cli)
        self.stdout.write(self.style.SUCCESS(f"{len(clientes)} clientes criados."))

        # 5. Criar Mesas
        for num in range(1, 6):
            Mesa.objects.update_or_create(
                numero=num, defaults={"status": "Livre", "capacidade": 4}
            )
        self.stdout.write(self.style.SUCCESS("5 mesas criadas."))

        # 6. Gerar Pedidos e Itens de Pedido Simulados
        mesas = list(Mesa.objects.all())
        for _ in range(10):
            mesa = random.choice(mesas)
            cliente = random.choice(clientes)

            pedido = Pedido.objects.create(
                cliente=cliente, mesa=mesa, status="Concluído", valor_total=0.00
            )

            total_pedido = 0
            for _ in range(random.randint(1, 3)):
                prod = random.choice(produtos)
                qtd = random.randint(1, 3)
                subtotal = prod.preco * qtd

                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=prod,
                    quantidade=qtd,
                    preco_unitario=prod.preco,
                    subtotal=subtotal,
                )
                total_pedido += subtotal

            pedido.valor_total = total_pedido
            pedido.save()

        self.stdout.write(self.style.SUCCESS("Pedidos de teste gerados com sucesso!"))
        self.stdout.write(
            self.style.HTTP_INFO(
                "Banco populado com sucesso e pronto para análises combinatórias!"
            )
        )
