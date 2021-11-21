from django.contrib import admin
from estoque.models import Saida

# Register your models here.
class SaidaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'data_saida')

admin.site.register(Saida, SaidaAdmin)