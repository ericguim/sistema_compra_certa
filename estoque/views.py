from django.shortcuts import render, redirect
from .models import Produto, Fornecedor
from datetime import datetime

def estoque(request):
    if not request.user.is_authenticated:
        return redirect('login')

    produtos = Produto.objects.all()
    fornecedores = Fornecedor.objects.all()
    data = datetime.date(datetime.now()).strftime('%d/%m/%Y')
    return render(request, 'estoque/estoque.html', {'produtos': produtos, 'fornecedores': fornecedores, 'data': data})

def analise(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'estoque/analise.html')