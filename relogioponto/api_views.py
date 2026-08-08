from rest_framework import viewsets
from .models import RegistroPonto
from .serializers import RegistroPontoSerializer


class RegistroPontoViewSet(viewsets.ModelViewSet):
    queryset = RegistroPonto.objects.select_related("funcionario").all()
    serializer_class = RegistroPontoSerializer
