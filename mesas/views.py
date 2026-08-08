import io
import qrcode
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Mesa
from .serializers import MesaSerializer


class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer


def mesas_dashboard_view(request):
    """Renderiza a interface visual e amigável para gerenciamento de Mesas."""
    return render(request, "mesas/dashboard_mesas.html")


def gerar_qrcode_mesa(request, mesa_id):
    """Gera e retorna um QR Code em formato PNG para uma mesa específica."""
    mesa = get_object_or_404(Mesa, id=mesa_id)
    url_cardapio = request.build_absolute_uri(f"/cardapio/{mesa.token_qrcode}/")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url_cardapio)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")
