from rest_framework import serializers
from .models import Mesa, Pedido, ItemPedido
from produtos.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "descricao", "preco", "disponivel"]


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = ["id", "numero", "capacidade", "status", "token_qrcode"]


class ItemPedidoSerializer(serializers.ModelSerializer):
    produto_nome = serializers.ReadOnlyField(source="produto.nome")
    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = ItemPedido
        fields = [
            "id",
            "produto",
            "produto_nome",
            "quantidade",
            "observacao",
            "preco_unitario",
            "subtotal",
        ]


class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, read_only=True)
    valor_total = serializers.ReadOnlyField()

    class Meta:
        model = Pedido
        fields = ["id", "mesa", "garcom", "status", "criado_em", "valor_total", "itens"]
