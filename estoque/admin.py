from django.contrib import admin
from .models import Produto, Fornecedor

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estoque')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor)