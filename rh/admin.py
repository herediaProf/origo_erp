from django.contrib import admin
from .models import RegistroPonto


@admin.register(RegistroPonto)
class RegistroPontoAdmin(admin.ModelAdmin):
    list_display = ("funcionario", "tipo", "data_hora", "observacao")
    list_filter = ("tipo", "data_hora", "funcionario")
    search_fields = ("funcionario__username", "funcionario__email")
