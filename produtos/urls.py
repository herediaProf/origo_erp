from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, produtos_dashboard_view, listar_produtos

router = DefaultRouter()
router.register(r"", ProdutoViewSet, basename="produto")

urlpatterns = [
    path("", produtos_dashboard_view, name="produtos_home"),  # Tela visual amigável
    path(
        "json/", listar_produtos, name="produtos_json"
    ),  # Endpoint JsonResponse legado
    path("api/", include(router.urls)),  # Endpoints do DRF em /api/produtos/api/
]
