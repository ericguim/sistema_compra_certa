from django.shortcuts import render, redirect
from estoque.models import Produto, Saida
from django.contrib import messages

def saida(request):
    # Get form values
    if request.method == 'POST':
        produto = request.POST.get('produto')
        
        if request.POST.get('quantidade') == '':
            messages.error(request, 'Quantidade não pode ser vazia')
            return redirect('saida')
        else:
            quantidade = request.POST.get('quantidade')
        
        if int(quantidade) > Produto.objects.get(id=produto).estoque:
            messages.error(request, 'Quantidade maior que o estoque atual')
            return redirect('saida')

        # Create new object
        saida = Saida(produto=Produto.objects.get(id=produto), quantidade=quantidade)

        # Save object
        saida.save()
        return redirect('saida')

    produtos = Produto.objects.all()

    return render(request, 'saida/saida.html', {'produtos': produtos})