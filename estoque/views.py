from django.shortcuts import render
from .models import Produto, Fornecedor

def estoque(request):
    produtos = Produto.objects.all()
    fornecedores = Fornecedor.objects.all()
    return render(request, 'estoque/estoque.html', {'produtos': produtos, 'fornecedores': fornecedores})