from django.contrib import admin
from .models import Produto, Fornecedor

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'peso_caixa', 'estoque', 'fornecedor')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor)