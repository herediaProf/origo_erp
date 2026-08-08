from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import EstoqueItemViewSet

router = DefaultRouter()
router.register(r"itens", EstoqueItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
