from django.contrib import admin
from estoque.models import Entrada

# Register your models here.
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'data_entrada', 'fornecedor', 'preco')

admin.site.register(Entrada, EntradaAdmin)