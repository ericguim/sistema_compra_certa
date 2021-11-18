from django.shortcuts import render
from estoque.models import Produto, Fornecedor

def entrada(request):
    produtos = Produto.objects.all()
    fornecedores = Fornecedor.objects.all()
    return render(request, 'entrada/entrada.html', {'produtos': produtos, 'fornecedores': fornecedores})