from django.contrib import admin
from . import models

@admin.register(models.Formulario)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = (
        'tipo',
        'descricao',
        'plataforma',
        'marca',
        'provedores',
        'datainicio',
        'datafim',
        'observacao',
        'created',
    )
    list_filter = ('plataforma', 'marca', 'provedores', 'datainicio', 'datafim',)
    search_fields = ['tipo', 'descricao', 'observacao']
