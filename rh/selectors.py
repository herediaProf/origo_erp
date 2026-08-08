# orgo_erp/rh/selectors.py
from django.db.models import Sum, F, DecimalField
from pedidos.models import Pedido  # Ajuste o import conforme sua estrutura


def relatorio_comissoes_por_funcionario():
    return (
        Pedido.objects.values("funcionario__nome", "funcionario__comissao_percentual")
        .annotate(
            total_vendido=Sum("valor_total"),
            comissao_gerada=Sum(
                F("valor_total") * F("funcionario__comissao_percentual") / 100.0,
                output_field=DecimalField(),
            ),
        )
        .order_by("-total_vendido")
    )
