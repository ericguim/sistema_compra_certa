from django.shortcuts import render, redirect
from estoque.models import Produto, Fornecedor, Entrada, Saida

def entrada(request):
    # Get form values
    if request.method == 'POST':
        produto = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')
        fornecedor = request.POST.get('fornecedor')
        if request.POST.get('preco') == '':
            preco = 0
        else:
            preco = request.POST.get('preco')

        # Create new object
        entrada = Entrada(produto=Produto.objects.get(id=produto), quantidade=quantidade, fornecedor=Fornecedor.objects.get(id=fornecedor), preco=preco)

        # Save object
        entrada.save()
        return redirect('entrada')

    produtos = Produto.objects.all()
    fornecedores = Fornecedor.objects.all()

    return render(request, 'entrada/entrada.html', {'produtos': produtos, 'fornecedores': fornecedores})