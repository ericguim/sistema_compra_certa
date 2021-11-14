from django.shortcuts import render


def estoque(request):
    return render(request, 'estoque/estoque.html', {})