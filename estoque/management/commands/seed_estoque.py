from django.core.management.base import BaseCommand
from produtos.models import Categoria, Produto
from decimal import Decimal


class Command(BaseCommand):
    help = "Popula o banco de dados com categorias e produtos iniciais para testes"

    def handle(self, *args, **kwargs):
        self.stdout.write("Criando categorias...")
        cat_bebidas, _ = Categoria.objects.get_or_create(
            nome="Bebidas", defaults={"descricao": "Refrigerantes, sucos e águas"}
        )
        cat_alimentos, _ = Categoria.objects.get_or_create(
            nome="Alimentos", defaults={"descricao": "Ingredientes e pratos prontos"}
        )
        cat_limpeza, _ = Categoria.objects.get_or_create(
            nome="Limpeza", defaults={"descricao": "Produtos de higienização"}
        )

        self.stdout.write("Criando produtos...")
        produtos_exemplo = [
            {
                "nome": "Refrigerante Cola 2L",
                "descricao": "Refrigerante sabor cola garrafa 2 litros",
                "preco": Decimal("12.50"),
                "categoria": cat_bebidas,
                "estoque_atual": 45,
                "disponivel": True,
            },
            {
                "nome": "Água Mineral 500ml",
                "descricao": "Água mineral sem gás 500ml",
                "preco": Decimal("3.50"),
                "categoria": cat_bebidas,
                "estoque_atual": 120,
                "disponivel": True,
            },
            {
                "nome": "Hambúrguer Artesanal 180g",
                "descricao": "Medalhão de carne bovina selecionada 180g",
                "preco": Decimal("22.90"),
                "categoria": cat_alimentos,
                "estoque_atual": 8,
                "disponivel": True,
            },
            {
                "nome": "Batata Frita Congelada 2kg",
                "descricao": "Pacote de batata palito pré-frita congelada 2kg",
                "preco": Decimal("35.00"),
                "categoria": cat_alimentos,
                "estoque_atual": 0,
                "disponivel": False,
            },
            {
                "nome": "Detergente Líquido 500ml",
                "descricao": "Detergente neutro para louças 500ml",
                "preco": Decimal("2.99"),
                "categoria": cat_limpeza,
                "estoque_atual": 30,
                "disponivel": True,
            },
        ]

        for p in produtos_exemplo:
            Produto.objects.get_or_create(
                nome=p["nome"],
                defaults={
                    "descricao": p["descricao"],
                    "preco": p["preco"],
                    "categoria": p["categoria"],
                    "estoque_atual": p["estoque_atual"],
                    "disponivel": p["disponivel"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Banco populado com sucesso!"))
