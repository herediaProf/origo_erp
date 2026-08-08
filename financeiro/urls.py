from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CaixaViewSet,
    VendaViewSet,
    RateioCaixinhaViewSet,
    financeiro_dashboard_view,
)

router = DefaultRouter()
router.register(r"caixas", CaixaViewSet)
router.register(r"vendas", VendaViewSet)
router.register(r"rateios", RateioCaixinhaViewSet)

urlpatterns = [
    path("dashboard/", financeiro_dashboard_view, name="financeiro_dashboard"),
    path("", include(router.urls)),
]
