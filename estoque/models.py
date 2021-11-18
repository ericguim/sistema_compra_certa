from django.db import models
from django.conf import settings
from django.utils import timezone


class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    nome = models.CharField(max_length=200)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    estoque = models.IntegerField(default=0)
    consumo_medio = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    estoque_minimo = models.IntegerField(default=0)
    estoque_maximo = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
    
    def adicionar(self, quantidade):
        self.estoque += quantidade
        self.save()
    
    def remover(self, quantidade):
        self.estoque -= quantidade
        self.save()

class Fornecedor(models.Model):
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
    
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200, blank=True)
    lead_time = models.IntegerField()
    entrega_segunda = models.BooleanField(default=False)
    entrega_terca = models.BooleanField(default=False)
    entrega_quarta = models.BooleanField(default=False)
    entrega_quinta = models.BooleanField(default=False)
    entrega_sexta = models.BooleanField(default=False)
    entrega_sabado = models.BooleanField(default=False)
    entrega_domingo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome

class Entrada(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    data = models.DateTimeField(default=timezone.now)

class Saida(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    data = models.DateTimeField(default=timezone.now)