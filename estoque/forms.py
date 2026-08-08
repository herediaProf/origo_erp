from django import forms
from produtos.models import Produto, Categoria


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "nome",
            "descricao",
            "preco",
            "categoria",
            "estoque_atual",
            "disponivel",
        ]
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "w-full bg-slate-800 border border-slate-700 rounded-lg p-3 text-white"
                }
            ),
            "descricao": forms.Textarea(
                attrs={
                    "class": "w-full bg-slate-800 border border-slate-700 rounded-lg p-3 text-white",
                    "rows": 3,
                }
            ),
            "preco": forms.NumberInput(
                attrs={
                    "class": "w-full bg-slate-800 border border-slate-700 rounded-lg p-3 text-white",
                    "step": "0.01",
                }
            ),
            "categoria": forms.Select(
                attrs={
                    "class": "w-full bg-slate-800 border border-slate-700 rounded-lg p-3 text-white"
                }
            ),
            "estoque_atual": forms.NumberInput(
                attrs={
                    "class": "w-full bg-slate-800 border border-slate-700 rounded-lg p-3 text-white"
                }
            ),
            "disponivel": forms.CheckboxInput(
                attrs={
                    "class": "w-5 h-5 text-teal-600 bg-slate-800 border-slate-700 rounded"
                }
            ),
        }
