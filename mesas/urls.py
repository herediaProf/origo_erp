from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MesaViewSet, mesas_dashboard_view, gerar_qrcode_mesa

router = DefaultRouter()
router.register(r"mesas", MesaViewSet, basename="mesa")

urlpatterns = [
    path("", mesas_dashboard_view, name="mesas_home"),  # Tela visual amigável
    path(
        "qrcode/<int:mesa_id>/", gerar_qrcode_mesa, name="mesa_qrcode"
    ),  # Endpoint para gerar QR Code
    path(
        "api/", include(router.urls)
    ),  # Endpoints da API REST JSON (/api/mesas/api/mesas/)
]
