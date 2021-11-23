from django.shortcuts import render
from .models import Produto, Fornecedor
from datetime import datetime

def estoque(request):
    produtos = Produto.objects.all()
    fornecedores = Fornecedor.objects.all()
    data = datetime.date(datetime.now()).strftime('%d/%m/%Y')
    return render(request, 'estoque/estoque.html', {'produtos': produtos, 'fornecedores': fornecedores, 'data': data})