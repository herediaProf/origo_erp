from django.urls import path
from .views import gerar_qrcode_mesa

urlpatterns = [
    path("mesa/<int:mesa_id>/qrcode/", gerar_qrcode_mesa, name="gerar_qrcode_mesa"),
]
