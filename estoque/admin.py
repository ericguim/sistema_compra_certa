from django.contrib import admin
from .models import Produto, Fornecedor

admin.site.register(Produto)
admin.site.register(Fornecedor)