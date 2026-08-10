from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from produtos.models import Produto, Categoria
from .forms import ProdutoForm


@login_required
def lista_estoque_view(request):
    """Lista todos os produtos e processa o cadastro rápido via formulário."""
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estoque:estoque_lista")
    else:
        form = ProdutoForm()

    # 'produtos' usado para manter compatibilidade direta com a listagem da tabela HTML
    produtos = Produto.objects.select_related("categoria").all().order_by("-id")

    context = {
        "produtos": produtos,
        "itens": produtos,  # Mantido caso algum outro template use 'itens'
        "titulo": "Gestão de Estoque e Produtos",
        "form": form,
    }
    return render(request, "estoque/lista_estoque.html", context)


@login_required
def salvar_produto_view(request, pk=None):
    """Cria ou edita um produto utilizando o ModelForm do Django."""
    produto_obj = get_object_or_404(Produto, pk=pk) if pk else None

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto_obj)
        if form.is_valid():
            form.save()
            return redirect("estoque:estoque_lista")
    else:
        form = ProdutoForm(instance=produto_obj)

    context = {
        "form": form,
        "item": produto_obj,
        "titulo": "Editar Produto" if produto_obj else "Novo Produto",
    }
    return render(request, "estoque/form_produto.html", context)


@login_required
def deletar_produto_view(request, pk):
    """Exclui um produto do estoque."""
    item = get_object_or_404(Produto, pk=pk)
    item.delete()
    return redirect("estoque:estoque_lista")
