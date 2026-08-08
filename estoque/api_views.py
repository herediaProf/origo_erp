from rest_framework import viewsets
from .models import EstoqueItem
from .serializers import EstoqueItemSerializer


class EstoqueItemViewSet(viewsets.ModelViewSet):
    queryset = EstoqueItem.objects.select_related(
        "fornecedor", "responsavel_compra"
    ).all()
    serializer_class = EstoqueItemSerializer
