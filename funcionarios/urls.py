from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import FuncionarioViewSet
from .views import funcionarios_view, salvar_funcionario, deletar_funcionario

router = DefaultRouter()
router.register(r"api", FuncionarioViewSet)  # Mantém a API em /funcionarios/api/

urlpatterns = [
    # Rotas Visuais (Telas HTML)
    path("", funcionarios_view, name="lista_funcionarios"),
    path("novo/", salvar_funcionario, name="novo_funcionario"),
    path("editar/<int:pk>/", salvar_funcionario, name="editar_funcionario"),
    path("deletar/<int:pk>/", deletar_funcionario, name="deletar_funcionario"),
    # Rotas da API REST
    path("", include(router.urls)),
]
