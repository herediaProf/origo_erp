from rest_framework import viewsets
from .models import Funcionario, RegistroPonto
from .serializers import FuncionarioSerializer, RegistroPontoSerializer
from django.shortcuts import render


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class RegistroPontoViewSet(viewsets.ModelViewSet):
    queryset = RegistroPonto.objects.all()
    serializer_class = RegistroPontoSerializer


def rh_dashboard_view(request):
    """Renderiza a interface visual de RH em vez de apenas o JSON da API"""
    return render(request, "rh/dashboard_rh.html")
