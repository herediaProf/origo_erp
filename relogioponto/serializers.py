from rest_framework import serializers
from .models import RegistroPonto


class RegistroPontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPonto
        fields = "__all__"
        read_only_fields = ("data_hora",)
