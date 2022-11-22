from rest_framework import serializers
from estoque.models import Produto, Fornecedor, Entrada, Saida

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ['url', 'id', 'nome', 'estoque', 'consumo_medio', 'estoque_minimo', 'estoque_maximo']

class FornecedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['url', 'id', 'nome', 'telefone', 'lead_time', 'entrega_segunda', 'entrega_terca', 'entrega_quarta', 'entrega_quinta', 'entrega_sexta', 'entrega_sabado', 'entrega_domingo']

class EntradaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrada
        fields = ['url', 'id', 'produto', 'quantidade', 'fornecedor', 'preco', 'data_entrada']

class SaidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Saida
        fields = ['url', 'id', 'produto', 'quantidade', 'data_saida']