from django.shortcuts import render, get_object_or_404, redirect
from .models import Funcionario


def funcionarios_view(request):
    """Renderiza a listagem visual de funcionários."""
    funcionarios = Funcionario.objects.all()
    return render(
        request, "funcionarios/lista_funcionarios.html", {"funcionarios": funcionarios}
    )


def salvar_funcionario(request, pk=None):
    """Cria ou edita um funcionário."""
    funcionario = get_object_or_404(Funcionario, pk=pk) if pk else None

    if request.method == "POST":
        nome = request.POST.get("nome")
        funcao = request.POST.get("funcao")
        cpf = request.POST.get("cpf")

        if funcionario:
            funcionario.nome = nome
            funcionario.funcao = funcao
            funcionario.cpf = cpf
            funcionario.save()
        else:
            Funcionario.objects.create(nome=nome, funcao=funcao, cpf=cpf)
        return redirect("/api/funcionarios/")

    # Define o título aqui na view para evitar tags condicionais no HTML
    titulo = "Editar Funcionário" if funcionario else "Novo Funcionário"

    return render(
        request,
        "funcionarios/form_funcionario.html",
        {"funcionario": funcionario, "titulo": titulo},
    )


def deletar_funcionario(request, pk):
    """Exclui um funcionário."""
    funcionario = get_object_or_404(Funcionario, pk=pk)
    funcionario.delete()
    return redirect("/funcionarios/")
