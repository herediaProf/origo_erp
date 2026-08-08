from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import MesaViewSet, ProdutoViewSet, PedidoViewSet, ItemPedidoViewSet
from .views import pedidos_dashboard_view  # <--- Importe a view aqui

router = DefaultRouter()
router.register(r"mesas", MesaViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"itens-pedido", ItemPedidoViewSet)

urlpatterns = [
    path(
        "dashboard/", pedidos_dashboard_view, name="pedidos_dashboard"
    ),  # <--- Adicione esta linha
    path("", include(router.urls)),
]
