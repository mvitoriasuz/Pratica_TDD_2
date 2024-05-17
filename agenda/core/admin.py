from django.contrib import admin
from .models import AgendaModel
from .forms import AgendaForm
from datetime import datetime


class AgendaModels(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'modificado_em', 'registrado_esse_ano', 'registrado_hoje')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome', 'cpf', 'telefone')
    list_filter = ('modificado_em',)

    def registrado_esse_ano(self, obj):
        hoje = datetime.today()
        return obj.modificado_em.year == hoje.year

    def registrado_hoje(self, obj):
        hoje = datetime.today()
        return obj.modificado_em.day == hoje.day and obj.modificado_em.month == hoje.month

    registrado_esse_ano.boolean = True
    registrado_hoje.boolean = True
    
admin.site.register(AgendaModel, AgendaModels)
