from rest_framework import serializers
from .models import Compra


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
        read_only_fields = ("data_compra",)
