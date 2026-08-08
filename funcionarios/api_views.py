from rest_framework import viewsets
from .models import Funcionario
from .serializers import (
    FuncionarioSerializer,
)  # Certifique-se de ter este serializer criado


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
