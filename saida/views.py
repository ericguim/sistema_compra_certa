from django.shortcuts import render, redirect
from estoque.models import Produto, Saida


def saida(request):
    # Get form values
    if request.method == 'POST':
        produto = request.POST.get('produto')
        
        if request.POST.get('quantidade') == '':
            quantidade = 0
        else:
            quantidade = request.POST.get('quantidade')

        # Create new object
        saida = Saida(produto=Produto.objects.get(id=produto), quantidade=quantidade)

        # Save object
        saida.save()
        return redirect('saida')

    produtos = Produto.objects.all()

    return render(request, 'saida/saida.html', {'produtos': produtos})