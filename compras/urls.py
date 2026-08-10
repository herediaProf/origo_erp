from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CompraViewSet
from . import views

router = DefaultRouter()
router.register(r"api", CompraViewSet)  # Rotas da API ficam sob /compras/api/

urlpatterns = [
    # Rotas para as telas HTML
    path("", views.compras_view, name="lista_compras"),
    path("novo/", views.salvar_compra, name="nova_compra"),
    path("editar/<int:pk>/", views.salvar_compra, name="editar_compra"),
    path("deletar/<int:pk>/", views.deletar_compra, name="deletar_compra"),
    # Rotas do Django REST Framework
    path("", include(router.urls)),
]
