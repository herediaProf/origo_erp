from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FuncionarioViewSet, RegistroPontoViewSet, rh_dashboard_view

router = DefaultRouter()
router.register(r"funcionarios", FuncionarioViewSet, basename="funcionario")
router.register(r"registros-ponto", RegistroPontoViewSet, basename="registroponto")

urlpatterns = [
    path(
        "", rh_dashboard_view, name="equipe_rh"
    ),  # Rota visual mapeada para o menu lateral!
    path(
        "api/", include(router.urls)
    ),  # APIs mantidas sob o prefixo /api/rh/api/ ou ajuste conforme preferir
]
