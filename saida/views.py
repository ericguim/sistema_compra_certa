from django.shortcuts import render
from estoque.models import Produto

def saida(request):
    produtos = Produto.objects.all()
    return render(request, 'saida/saida.html', {'produtos': produtos})