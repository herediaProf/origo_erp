import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from funcionarios.models import Funcionario
from .models import RegistroPonto


@csrf_exempt  # Usado para permitir o envio via fetch (AJAX) sem erro de token em testes iniciais
def relogioponto_view(request):

    # 1. Lógica para SALVAR o ponto (POST)
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            funcionario_id = data.get("funcionario_id")
            tipo = data.get("tipo")  # Ex: 'ENTRADA', 'SAIDA_ALMOCO', etc.

            if not funcionario_id or not tipo:
                return JsonResponse(
                    {"sucesso": False, "mensagem": "Dados incompletos."}, status=400
                )

            funcionario = Funcionario.objects.get(id=funcionario_id)

            # Criando o registro no banco
            RegistroPonto.objects.create(funcionario=funcionario, tipo=tipo)

            return JsonResponse(
                {
                    "sucesso": True,
                    "mensagem": f"Ponto de {tipo.replace('_', ' ').title()} registrado com sucesso!",
                }
            )

        except Funcionario.DoesNotExist:
            return JsonResponse(
                {"sucesso": False, "mensagem": "Funcionário não encontrado."},
                status=404,
            )
        except Exception as e:
            return JsonResponse({"sucesso": False, "mensagem": str(e)}, status=500)

    # 2. Lógica para CARREGAR a página (GET)
    funcionarios = Funcionario.objects.all().order_by("nome")
    context = {
        "funcionarios": funcionarios,
    }
    return render(request, "ponto.html", context)
