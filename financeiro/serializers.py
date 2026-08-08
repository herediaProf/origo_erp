from rest_framework import serializers
from .models import Caixa, Venda, RateioCaixinha


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = "__all__"
        read_only_fields = ("data_venda",)


class CaixaSerializer(serializers.ModelSerializer):
    vendas = VendaSerializer(many=True, read_only=True)

    class Meta:
        model = Caixa
        fields = "__all__"
        read_only_fields = ("data_abertura", "data_fechamento")


class RateioCaixinhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateioCaixinha
        fields = "__all__"
        read_only_fields = ("data_rateio",)
