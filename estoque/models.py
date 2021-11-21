from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta, date
import math


class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    nome = models.CharField(max_length=200)
    #fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    estoque = models.IntegerField(default=0)
    consumo_medio = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    estoque_minimo = models.IntegerField(default=0)
    estoque_maximo = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
    
    def adicionar(self, quantidade):
        self.estoque += int(quantidade)
        self.save()
    
    def remover(self, quantidade):
        self.estoque -= int(quantidade)
        self.save()

    def previsao_estoque_minimo(self):
        if self.estoque < self.estoque_minimo:
            return datetime.date(datetime.now()).strftime('%d/%m/%Y')
        elif self.consumo_medio == 0:
            data = datetime.date(datetime.now()) + timedelta(days=math.floor((self.estoque - self.estoque_minimo) / 1))
            return data.strftime('%d/%m/%Y')
        else:
            data = datetime.date(datetime.now()) + timedelta(days=math.floor((self.estoque - self.estoque_minimo) / self.consumo_medio))
            return data.strftime('%d/%m/%Y')

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
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.DO_NOTHING, null=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    data_entrada = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.produto.adicionar(self.quantidade)
        super(Entrada, self).save(*args, **kwargs)


class Saida(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    data_saida = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.produto.remover(self.quantidade)
        super(Saida, self).save(*args, **kwargs)