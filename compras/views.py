from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from .models import Compra
from fornecedores.models import Fornecedor
from funcionarios.models import Funcionario


def compras_view(request):
    """Renderiza a listagem de compras."""
    compras = Compra.objects.select_related("fornecedor", "comprador").all()
    return render(request, "compras/lista_compras.html", {"compras": compras})


def salvar_compra(request, pk=None):
    """Cria ou edita uma compra."""
    compra = get_object_or_404(Compra, pk=pk) if pk else None
    fornecedores = Fornecedor.objects.all()
    funcionarios = Funcionario.objects.all()

    if request.method == "POST":
        fornecedor_id = request.POST.get("fornecedor")
        comprador_id = request.POST.get("comprador")
        valor_total = request.POST.get("valor_total")
        status = request.POST.get("status")
        observacoes = request.POST.get("observacoes")

        try:
            fornecedor = get_object_or_404(Fornecedor, pk=fornecedor_id)
            comprador = (
                Funcionario.objects.filter(pk=comprador_id).first()
                if comprador_id
                else None
            )

            if compra:
                compra.fornecedor = fornecedor
                compra.comprador = comprador
                compra.valor_total = valor_total
                compra.status = status
                compra.observacoes = observacoes
                compra.save()
            else:
                Compra.objects.create(
                    fornecedor=fornecedor,
                    comprador=comprador,
                    valor_total=valor_total,
                    status=status,
                    observacoes=observacoes,
                )
            return redirect("/compras/")

        except IntegrityError:
            context = {
                "compra": compra,
                "fornecedores": fornecedores,
                "funcionarios": funcionarios,
                "erro": "Erro de integridade ao salvar a compra. Verifique os dados.",
            }
            return render(request, "compras/form_compra.html", context)

    context = {
        "compra": compra,
        "fornecedores": fornecedores,
        "funcionarios": funcionarios,
        "status_choices": Compra.STATUS_CHOICES,
    }
    return render(request, "compras/form_compra.html", context)


def deletar_compra(request, pk):
    """Exclui uma compra."""
    compra = get_object_or_404(Compra, pk=pk)
    compra.delete()
    return redirect("/compras/")
