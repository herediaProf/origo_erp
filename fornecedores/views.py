from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Fornecedor


@login_required
def lista_fornecedores_view(request):
    """Lista todos os fornecedores cadastrados."""
    fornecedores = Fornecedor.objects.all().order_by("-id")
    context = {"fornecedores": fornecedores, "titulo": "Gestão de Fornecedores"}
    return render(request, "fornecedores/lista_fornecedores.html", context)


@login_required
def salvar_fornecedor_view(request, pk=None):
    """Cria ou edita um fornecedor."""
    fornecedor_obj = get_object_or_404(Fornecedor, pk=pk) if pk else None

    if request.method == "POST":
        nome = request.POST.get("nome")
        cnpj_cpf = request.POST.get("cnpj_cpf") or None
        telefone = request.POST.get("telefone") or None
        email = request.POST.get("email") or None

        if fornecedor_obj:
            fornecedor_obj.nome = nome
            fornecedor_obj.cnpj_cpf = cnpj_cpf
            fornecedor_obj.telefone = telefone
            fornecedor_obj.email = email
            fornecedor_obj.save()
        else:
            Fornecedor.objects.create(
                nome=nome, cnpj_cpf=cnpj_cpf, telefone=telefone, email=email
            )

        return redirect("fornecedores_web:fornecedores_lista")

    context = {
        "fornecedor": fornecedor_obj,
        "titulo": "Editar Fornecedor" if fornecedor_obj else "Novo Fornecedor",
    }
    return render(request, "fornecedores/form_fornecedor.html", context)


@login_required
def deletar_fornecedor_view(request, pk):
    """Exclui um fornecedor."""
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    fornecedor.delete()
    return redirect("fornecedores_web:fornecedores_lista")
