import qrcode
import io
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from .models import Mesa


def gerar_qrcode_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)

    # URL que o cliente vai abrir ao ler o QR Code (ex: IP do servidor ou domínio de produção)
    # Aqui apontamos para a rota do cardápio digital daquela mesa específica usando o token único
    url_cardapio = f"http://127.0.0.1:8000/cardapio/{mesa.token_qrcode}/"

    # Gerar a imagem do QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url_cardapio)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Salvar a imagem em um buffer de memória
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer, content_type="image/png")
