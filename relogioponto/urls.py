from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import RegistroPontoViewSet

router = DefaultRouter()
router.register(r"", RegistroPontoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
