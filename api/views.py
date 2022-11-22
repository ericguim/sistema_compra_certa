from estoque.models import Produto, Fornecedor, Entrada, Saida
from rest_framework import viewsets
from .serializers import ProdutoSerializer, FornecedorSerializer, EntradaSerializer, SaidaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    Endpoint API que fornece uma lista de produtos cadastrados.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    """
    Endpoint API que fornece uma lista de fornecedores cadastrados.
    """
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class EntradaViewSet(viewsets.ModelViewSet):
    """
    Endpoint API que fornece uma lista de entradas realizadas.
    """
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class SaidaViewSet(viewsets.ModelViewSet):
    """
    Endpoint API que fornece uma lista de saídas realizadas.
    """
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer