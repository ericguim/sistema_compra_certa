from django.shortcuts import render, redirect
from estoque.models import Produto, Fornecedor, Entrada, Saida
from django.contrib import messages

def entrada(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Get form values
    if request.method == 'POST':
        produto = request.POST.get('produto')
        fornecedor = request.POST.get('fornecedor')

        if int(request.POST.get('quantidade')) == 0:
            messages.error(request, 'Quantidade não pode ser 0')
            return redirect('entrada')

        quantidade = request.POST.get('quantidade')

        if request.POST.get('preco') == '':
            preco = 0
        else:
            preco = request.POST.get('preco')

        # Create new object
        entrada = Entrada(produto=Produto.objects.get(id=produto), quantidade=quantidade, fornecedor=Fornecedor.objects.get(id=fornecedor), preco=preco)

        # Save object
        entrada.save()
        messages.success(request, 'Entrada cadastrada com sucesso')
        return redirect('entrada')

    produtos = Produto.objects.all()
    fornecedores = Fornecedor.objects.all()

    return render(request, 'entrada/entrada.html', {'produtos': produtos, 'fornecedores': fornecedores})