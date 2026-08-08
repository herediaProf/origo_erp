from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CompraViewSet

router = DefaultRouter()
router.register(r"", CompraViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
