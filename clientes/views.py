from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente


def clientes_view(request):
    """Renderiza a listagem de clientes."""
    clientes = Cliente.objects.all()
    return render(request, "clientes/lista_clientes.html", {"clientes": clientes})


def salvar_cliente(request, pk=None):
    """Cria ou edita um cliente."""
    cliente = get_object_or_404(Cliente, pk=pk) if pk else None

    if request.method == "POST":
        nome = request.POST.get("nome")
        cpf_cnpj = request.POST.get("cpf_cnpj")
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")

        if cliente:
            cliente.nome = nome
            cliente.cpf_cnpj = cpf_cnpj
            cliente.telefone = telefone
            cliente.email = email
            cliente.save()
        else:
            Cliente.objects.create(
                nome=nome, cpf_cnpj=cpf_cnpj, telefone=telefone, email=email
            )
        return redirect("/clientes/")

    return render(request, "clientes/form_cliente.html", {"cliente": cliente})


def deletar_cliente(request, pk):
    """Exclui um cliente."""
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect("/clientes/")
