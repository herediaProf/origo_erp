from rest_framework import serializers
from .models import Funcionario, RegistroPonto


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = "__all__"


class RegistroPontoSerializer(serializers.ModelSerializer):
    funcionario_nome = serializers.CharField(
        source="funcionario.username", read_only=True
    )

    class Meta:
        model = RegistroPonto
        fields = "__all__"
