from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import FuncionarioViewSet

router = DefaultRouter()
router.register(r"", FuncionarioViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
