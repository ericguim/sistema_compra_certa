from django.contrib import admin

from estoque.views import estoque
from .models import Produto, Fornecedor

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estoque', 'consumo_medio', 'estoque_minimo', 'estoque_maximo')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor)