from django.shortcuts import render, redirect
from estoque.models import Produto, Fornecedor

def entrada(request):
    produtos = Produto.objects.all()
    fornecedores = Fornecedor.objects.all()

    if request.method == 'POST':
        # produto = Produto()
        print(request.POST)
        return redirect('entrada')

    return render(request, 'entrada/entrada.html', {'produtos': produtos, 'fornecedores': fornecedores})