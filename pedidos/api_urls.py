from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import MesaViewSet, ProdutoViewSet, PedidoViewSet, ItemPedidoViewSet

router = DefaultRouter()
router.register(r"mesas", MesaViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"itens-pedido", ItemPedidoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
